#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class TurtleBot:

    def __init__(self):
	
        rospy.init_node('turtlebot_goal', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

	#This function is called when a new message of type Pose is received by the subscriber.
    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

	#Euclidean distance between current pose and the goal.
    def euclidean_distance(self, goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
	
    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

	#The move2goal method will be the one which moves the turtle. 
    def move2goal(self):
	
        goal_pose = Pose()

        goal_pose.x = input("Set your x goal: ")
        goal_pose.y = input("Set your y goal: ")
        distance_tolerance = input("Set your tolerance: ")

        vel_msg = Twist()

		#Please, insert a number slightly greater than 0 (e.g. 0.01).
        while self.euclidean_distance(goal_pose) >= distance_tolerance:

            # Linear velocity in the x-axis.
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        # If we press control + C, the node will stop. Otherwise, it still exists
        rospy.spin()

#Finally, we call our function move2goal after having created an object x of type TurtleBot:
if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass
