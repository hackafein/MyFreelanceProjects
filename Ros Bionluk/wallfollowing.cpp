#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>

#include <tr1/tuple>
#include <sstream>
#include <algorithm>

///////////////////////////////////
//////////// CONSTANTS ////////////
///////////////////////////////////
const float MOVEMENT_SPEED = 0.05;
const float TURN_RATE  = 0.15;

const float FOLLOW_DISTANCE = 0.3; 
const float SAFE_DISTANCE = 0.15; 

const int MAX_SCAN_REP = 5;

// Used to detect how far of a difference in readings consists of a corner
const float CORNER_DROPOFF_DELTA = 0.1;

// A few actions move and turn, this is the delay between the two
const float TURN_WAIT_TIME_SECONDS = 0.5;

///////////////////////////////////
////////////// ENUMS //////////////
///////////////////////////////////

// Enums -- In part 1, SLINE just moves the robot forward.
enum PlanningPhase { SLINE, WALL, CORNER };
enum CornerSubPhase { MOVE, TURN };
enum Direction { LEFT, CENTER, RIGHT, NONE };

///////////////////////////////////
///////// STATE VARIABLES /////////
///////////////////////////////////
int CurrentPhase;         // What planning phase the robot is in
int CurrentCornerPhase;   // How far we are in our process of turning corners
int Num_Points;           // The number of points in the raw scan
float Raw_Scan[360];      // The raw readings by the scanner
float Smoothed_Scan[3];   // Closest points of the Left, Right, Middle parts of the scan
int CurrentScanRep;       // Current repetition of the scan
int FollowWallSide;       // Tells use which side the wall we're following is on/should be
float PreviousWallDist;

///////////////////////////////////
////////// ROS VARIABLES //////////
///////////////////////////////////
ros::Publisher Velocity_publisher;
geometry_msgs::Twist Cmd;

///////////////////////////////////
/////// METHOD DECLARATIONS ///////
///////////////////////////////////
void ProcessLaserScan(const sensor_msgs::LaserScan::ConstPtr& scan);
void PlanPath();
void WallPhase();
void SlinePhase();
void CornerPhase();

///////////////////////////////////
///// MAIN AND HELPER METHODS /////
///////////////////////////////////
int main(int argc, char **argv)
{
	ros::init(argc, argv, "wall_follow");

	ROS_INFO("Lets start!");

	// Ros create a Node Handle
	ros::NodeHandle n;
	Velocity_publisher = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1);

	// Robot state initialization
	CurrentPhase = SLINE;
	FollowWallSide = NONE;
	PreviousWallDist = 9999;

	// All systems ready. BEGIN.
	ros::Subscriber sub = n.subscribe<sensor_msgs::LaserScan>("/scan", 1, ProcessLaserScan);
	ros::spin();
}

void Forward(float dist)
{
	Cmd.linear.x = dist;
	Cmd.linear.y = 0;
	Cmd.linear.z = 0;
	Cmd.angular.x = 0;
	Cmd.angular.y = 0;
	Cmd.angular.z = 0;

	Velocity_publisher.publish(Cmd);
}

void Turn(float rad)
{
	Cmd.linear.x = 0;
	Cmd.linear.y = 0;
	Cmd.linear.z = 0;
	Cmd.angular.x = 0;
	Cmd.angular.y = 0;
	Cmd.angular.z = rad;

	Velocity_publisher.publish(Cmd);
}

// Turn away from the wall being followed
void TurnAway(float rad)
{
  	// Turn away from the wall we're following -- we've reached a corner
	int turnModifier = 1;

	if(FollowWallSide == LEFT)
	{
		turnModifier = -1;
	}

	Turn(turnModifier * rad);
}

// Returns <dist, side> for the smoothed vision.
// Returns a distance of 9999 and side of NONE if everything is out of range
std::tr1::tuple<float, int> GetClosestPointAndDirection()
{
	float smallest = 9999;
	int side = NONE;

	if(Smoothed_Scan[0] < smallest && Smoothed_Scan[0] != 0)
	{
		smallest = Smoothed_Scan[0];
		side = LEFT;
	}

	if(Smoothed_Scan[1] < smallest && Smoothed_Scan[1] != 0)
	{
		smallest = Smoothed_Scan[1];
		side = RIGHT;
	}

	if(Smoothed_Scan[2] < smallest && Smoothed_Scan[2] != 0)
	{
		smallest = Smoothed_Scan[2];		
		side = CENTER;
	}

	return std::tr1::make_tuple(smallest, side);
}

// Finds the closest point in the Raw Scan reading from start (inclusive) to end (exclusive).
// Called by MakeSmoothScan()
float GetClosestPointInRange(int start, int end)
{
	float smallest = 9999;

	for(int i = start; i < end; i++)
	{
		//printf("%d %.2f\n", i, Raw_Scan[i]);
		if(Raw_Scan[i] == Raw_Scan[i] && Raw_Scan[i] != 0 && smallest > Raw_Scan[i])
		{
			smallest = Raw_Scan[i];
		}
	}

	return smallest;
}

// Calculates the closest points of the left, right and center points
// for smoothed vision
void MakeSmoothScan()
{
	const int right_index_start = 0;
	const int right_index_end = 90;
	const int left_index_start = 270;
	const int Left_index_end = 360;

	//Turtlebot3
	Smoothed_Scan[0] = GetClosestPointInRange(270, 330);
	Smoothed_Scan[1] = GetClosestPointInRange(30, 90);
	Smoothed_Scan[2] = std::min(GetClosestPointInRange(330, 360), GetClosestPointInRange(0, 30));
}

///////////////////////////////////
///////// PLANNER METHODS /////////
///////////////////////////////////

// Scan the number of times specified by maxScanRep before moving. This is to prevent magical NaN misreads.
// Then take the smallest non-NaN reading or use NaN if that was all that was read to plan the next move.
void ProcessLaserScan(const sensor_msgs::LaserScan::ConstPtr& scan)
{
	// Length of scan array
        // http://docs.ros.org/melodic/api/sensor_msgs/html/msg/LaserScan.html
	Num_Points =  (int)(scan->angle_max - scan->angle_min) / scan->angle_increment;

	//printf("Num_Points: %d\n", Num_Points);

	// Copy everything from the first scan into the local scan array
	// After that only copy non non-NaN values.
	if(CurrentScanRep < MAX_SCAN_REP)
	{
		for(int i = 0; i < Num_Points; i++)
		{
			if(CurrentScanRep == 0)
			{
				Raw_Scan[i] = scan->ranges[i];
			}
			else if(Raw_Scan[i] == Raw_Scan[i])
			{
				Raw_Scan[i] = scan->ranges[i];
			}
		}
		CurrentScanRep++;
	}
	else // 5 scans complete
	{
		// Move
		MakeSmoothScan();
		PlanPath();

		// Reset the scan counter
		CurrentScanRep = 0;
	}
}

void PlanPath()
{
	switch(CurrentPhase)
	{
		case SLINE:
			printf("SLINE\n");
			SlinePhase();
			break;

		case CORNER:
			printf("CORNER\n");
			CornerPhase();
			break;

		case WALL:
		default:
			printf("WALL\n");
			WallPhase();
			break;
	}

	PreviousWallDist = Smoothed_Scan[FollowWallSide];
}

// In the wall runner code, this moves forward only until a wall comes within following distance.
// The robot runs this function to follow the SLine.
// Then it will check for a wall in front.
void SlinePhase()
{
	std::tr1::tuple<float, int> point = GetClosestPointAndDirection();
	
	float smallest = std::tr1::get<0>(point);
	int side = std::tr1::get<1>(point);

	if(smallest > FOLLOW_DISTANCE || smallest == 0) // safe and not following wall
	{
		Forward(MOVEMENT_SPEED);
	}
	else if(smallest > SAFE_DISTANCE) // safe < smallest < follow, start following that wall
	{
		CurrentPhase = WALL;

		// Pick a side to put the wall and change the phase
		if(side == CENTER)
		{
			if(Smoothed_Scan[LEFT] < Smoothed_Scan[RIGHT])
			{
				FollowWallSide = LEFT;
			}
			else
			{
				FollowWallSide = RIGHT;
			}
		}
		else if(side == RIGHT)
		{
			FollowWallSide = RIGHT;
		}
		else
		{
			FollowWallSide = LEFT;
		}

		PreviousWallDist = Smoothed_Scan[FollowWallSide];
	}
	else // too close to wall -- REVERSE THRUSTERS ACTIVATE
	{
		Forward(-1 * MOVEMENT_SPEED);
	}
}

// This phase is responsible for following the wall.
// The robot will adjust itself based on its proximity to the wall it has decided to follow.
void WallPhase()
{
	// Turn away if there is a wall in front
	if(Smoothed_Scan[CENTER] < SAFE_DISTANCE)
	{
		std::cout << "Wall Phase Function Center\n";
		TurnAway(TURN_RATE * 2);
	}
	else // No wall in front of us
	{
		float wallDist = Smoothed_Scan[FollowWallSide];

		if( abs(PreviousWallDist - wallDist) > CORNER_DROPOFF_DELTA) // Dropoff was too big, we just saw a corner (or similar)
		{
			std::cout << "Wall Phase Function Corner\n";
			CurrentPhase = CORNER;
			CurrentCornerPhase = MOVE;
		}		
		else if(wallDist < SAFE_DISTANCE)   // Turn away if the wall we're following is too close
		{
			TurnAway(TURN_RATE);
		}
		else if(wallDist > FOLLOW_DISTANCE) // Wall too far but not corner, turn towards it
		{
			std::cout << "Wall Phase Function wallDist > FOLLOW_DISTANCE TurnAway(-1*TURN_RATE)\n";
			TurnAway(-1*TURN_RATE);
			ros::Duration(TURN_WAIT_TIME_SECONDS).sleep();
			Forward(MOVEMENT_SPEED/2);
		}		
		else // Distance is just right
		{
			std::cout << "Wall Phase Function Forward(MOVEMENT_SPEED)\n";
			Forward(MOVEMENT_SPEED);
		}
	}
}

void CornerPhase()
{
	if(CurrentCornerPhase == MOVE) // Try to get a good ways into the doorway or distance
	{
		float boost_into_doorway_speed = 0.2;

		std::cout << "Corner Phase Function Move\n";
		TurnAway(TURN_RATE * 2);
		ros::Duration(TURN_WAIT_TIME_SECONDS).sleep();
		Forward(boost_into_doorway_speed); // Get a good ways into the doorway
		CurrentCornerPhase = TURN;
	}
	else if(CurrentCornerPhase == TURN)
	{
		std::cout << "Corner Phase Function Turn\n";

		// Turn towards the wall until we can see the wall again and then follow it
		if(Smoothed_Scan[FollowWallSide] < FOLLOW_DISTANCE)
		{
			CurrentPhase = WALL;
			CurrentCornerPhase = 0;
		}
		else
		{
			TurnAway(-1 * TURN_RATE);
		}
	}
}

// Reference: wall_follow.cpp from https://github.com/


