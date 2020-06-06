"""
Istanbul Sehir University
ENGR101 - Introduction to Programming
Mini Project 4 - Project Template 
library Management System

Notes:
1. You have to use this template
2. You should fill the attributes and the methods
3. Please read the PDF carefully before starting
4. "TODO" statements will give you the general idea about each part
5. To have a clear understanding please use the attached executable file to test the project and check how it works
"""


class MenuItem:
    """ This class initialises Item for a menu """

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        self.menu_items=[]      #Defining menu_items
        
        pass

    def display(self):
        """ This method displays item menu """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below
        for i in len(self.menu_items):      # This section is for publishing our menu options for user and admin.
            print(i+"-)"+self.menu_items)
        pass


class Menu():
    """ This class initialises a menu """

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        self.header= """
                        ::::::::::::::::::::::::::::::::::::::::::::
                        ****​Welcome to Library Management System​**** 
                        ::::::::::::::::::::::::::::::::::::::::::::        
                    """
        self.display_header=True                        #This section is for Menu headers
        pass            

    def display(self,templist):
        """ This method displays menu instance """
        #  TODO: implement the method to print the menu items here with the header according to the flag
        # write your code below
        if self.display_header==True:                   # This is for displaying Headers
            print(self.header)
        for i in range(1,len(templist)):                # Shows menu options
            print(str(i)+"-)"+ templist[i])
            
        pass

    def add_menu_item(self,new_item):
        """ This method adds menu item """
        # TODO: implement the method to add menu items by creating an object of MenuItem class here and adding it to
        #  the list (instance level attribute "menuItems") of this class. At the end of this method return a string
        #  states that the menuitem has been successfully added write your code below
        
        

        pass


class User:
    """ This class initialises user instance """
    #  TODO: initialise the class level attributes here
    # write your code below
    pass

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        self.menu=""
        self.menu_items=[]              # We determine the initial values of our users
        self.name=""
        self.password=""
        self.admin_menu=["List books","Create a book","Delete a book","Search for a book","Change number of a copies of a book", "Show students borrowed a book by ""ID","List Users", "Create User","Delete User", "Exit"]
        self.student_menu=["Search for a book","Add a book to my book list","delete a book from my book list","show my borrowed books", "Exit"]


        pass

    def display(self):
        """ This method displays user instance """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below
        print("Name:"+str(self.name),"Password:"+str( self.password))   #This shows display results
        pass

    def menu_builder(self,menulist):
        """ This method build the default menus for admin and student """
        # TODO: implement the method to build the menu here by using the class level attribute "menu" and its method
        #  "add_menu_item" write your code below
        templist=[]
        for i in menulist:
            
            templist.append(i)
        Menu().display(templist)        #This is actual menu listers

        return templist


        pass


class Admin(User):
    #  TODO: inherit the user class
    #  TODO: initialise the class level attributes here
    # write your code below
    
    pass

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        Menu.header=("Welcome Admin!!!")            #When the admin logs in this header comes out!
        self.role=("admin")                         #We determine our admins role for admin
        self.admin_menu=["List books","Create a book","Delete a book","Search for a book",      #and we put our books
"Change number of a copies of a book", "Show students borrowed a book by ""ID",
"List Users", "Create User","Delete User", "Exit"]
        self.menu_builder(self.admin_menu)
        
        pass


class Student(User):
    #  TODO: inherit the user class
    #  TODO: initialise the class level attributes here
    # write your code below
    
    pass

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        self.student_menu=["Search for a book","Add a book to my book list","delete a book from my book list","show my borrowed books", "Exit"]
        self.menu_builder(self.student_menu)
        pass


class UsersDB:
    """ This class initialises the the DB for user instances """
    #  TODO: initialise the class level attributes here
    # write your code below
    pass

    def __init__(self):
        #  TODO: implement the method to call the "create_example_users" function here according to the flag
        # write your code below
        self.example_users = {'Ahmet': ['1234', 'student'], 'Ayse': ['4321', 'student'], "admin": #this is a database which saves the users
["0000", 'admin']}
        self.user_object="" 
        self.example_users_flag = True      
        
        pass

    def create_example_users(self):
        """ This method creates example users to be used in this demo """  
        # TODO: implement the method to add the example users by using "add_user" function and return a string that
        #  shows it has been added successfully write your code below
        # write your code below
        

        pass

    def add_user(self):
        """ This method adds a user to users DB """
        #  TODO: implement the method to create Student/Admin object according to the role and add it the class level
        #   instance "users_objects and return a string that shows it has been added successfully
        # write your code below
        usr=input("What is the name of the user that you want to add?:")
        passw=input("What is the password of the as user that you want to add?")
        
        self.example_users[str(urs)] = [passw,"student"]    #This lines adds our new users
        pass

    def remove_user(self):
        """ This method removes a user from users DB """
        #  TODO: implement the method to remove a user by the name after listing all the users by "list_user" function
        # write your code below
        list_user(self)
        usr=input("What is the name of the user that you want to add?:")
        del self.example_users[usr]         #We delete user from our USERDB 
        pass

    def list_user(self):
        """ This method list all users in the users db """
        # TODO: implement the method to list all student users and return a string that shows it has been added
        #  successfully write your code below
        # write your code below
        for key,value in self.example_users.items(): #  thisloops gives us a list which is user name
            print(key)
            
        pass

    def validate_user(self,uid,password):               #this is for controlling login interfaces
        """ This method validate user credentials """
        # TODO: implement the method to check username and password and return the username in terms of correct
        #  credentials and False in terms of wrong credentials
        # write your code below
        
        try: 
            UsersDB().example_users[uid][0] == password 
            print("Successfully logged in!")                # success condition
            return UsersDB().example_users[uid][1]
        except:
            print("Invalid id or password please try again") #İnvalid login option
            return False
                

        
        pass


class Book:
    """ This class initialises the book instances """

    def __init__(self):                     #books
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        self.bid=""     
        self.name=""                                    #Our books initial values
        self.no_of_copies=""
        self.list_of_authors=[]

        pass

    def display(self):
        """ This method displays book instances """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below
                                                    #This line shows us books info
        print("Book id : "+self.bid+", Book Name: "+self.name+", Number of Copies: "+self.no_of_copies+", Book Authors: "+str(self.list_of_authors)+" ")
        pass


class Library:
    """ This class initialises the library system """
    #  TODO: initialise the class level attributes here
    # write your code below

    pass

    def __init__(self):
        #  TODO: implement the method to call the function "create_example_books" according to the flag
        # write your code below
        self.example_books = {"001": ["Biology", 2, ["Alice", "Bob"]], "002": ["Chemistry", 3,["Alice"]]}   #Book database

        pass

    def create_example_books(self):
        """ This method creates example books to be used """
        # TODO: implement the method to create the example books by using "add_book" function and return a string
        #  that shows it has been created successfully
        # write your code below
        Book.bid=input("What is the id of the book that you want to add?:")
        Book.name=input("What is the name of the "+ Book.bid +" book that you want to add?:")
        Book.no_of_copies=input("What is the number of the copies of the "+Book.name + "book that you want to add?:")   #add book to database
        Book.list_of_authors=input("Who are the authors of "+Book.name + " book?:")
        Book().display
        
        pass

    def add_book(self):
        """ This method adds book to the library """
        # TODO: implement the method to add book by creating Book class object and to add it to the class level
        #  attribute "book_objects" and return a string that shows it has been added successfully
        # write your code below
        self.example_books[str(Book.bid)] = [Book.name,Book.no_of_copies,Book.list_of_authors]
        print("Book has been successfully added")
        pass

    def remove_book(self,bid):
        """ This method removes book from the library """
        # TODO: implement the method to remove book by its id after listing all the books by list_book function (dont
        #  forget to remove it from the author to books list) and return a string shows the status (deleted/not found)
        # write your code below
        del self.example_books[str(Book.bid)]           #delete books
        print("Book has been successfully deleted")
        pass

    def list_book(self):
        """ This method lists all the library in the library """
        # TODO: implement the method to list all books and return a string shows that all books have been listed
        # write your code below
        for key,value in self.example_books.items():        #loops for listing books
            print(key)
            
        
        pass

    def search_book(self):
        """ This method searches the library for a specific book """
        # TODO: implement the method to search for a book by author name or book name and return a string shows the
        #  status (Matched books/No books)
        # write your code below
        pass

    def update_book_copies(self):
        """ This method updates the number of copies of a specific book """
        # TODO: implement the method to update the copies number of a book after listing all the books and return a
        #  string shows the status (book updated/no book with this id/new value smaller than the number of students
        #  holding the book)            
        # write your code below
        pass


class Main:
    """ This class is the main class of the library management system """

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        self.library=True
        self.userDB=True
        self.current_user=None      #initial main flags
        self.login_condition=False
        self.choose_action=True
        pass

    def login(self):
        """ This method deals with the login process """
        # TODO: implement the method to deal with the login attempts by using validate_user function from userDB
        #  instance and printing the required messages. In terms of success attempt, the method should call
        #  show_student_menu or show_admin_menu
        # write your code below

        
        
        while self.login_condition==False:                                          # BASE LOGİN AREA
                uid=str(input("Please Enter your Username= "))
                self.password=str(input("Please Enter your Password= "))
                self.login_condition=UsersDB.validate_user(self,uid,self.password)

        if self.login_condition!=False:
            self.current_user=uid
        
        if self.login_condition=="admin":
            Main.show_admin_menu(self)                              #Detecting who is the user?
        elif self.login_condition=="student":
            Main.show_student_menu(self)

        


        pass

    def show_admin_menu(self):
        """ This method shows the admin menu and do redirection """
        #  TODO: implement the method to welcome the admin and show the admin menu by using current_user value and do
        #   the redirection to the methods according to the choice with the required implementations
        # write your code below
        print("Dear admin, Welcome to admin menu")                  # If it is admin we call him admin
        
        Admin().__init__()
        adminmenu=User().admin_menu                         # we define our menu interface for admin speccialy
        while self.choose_action==True:
            choose=int(input("Your choose = "))
            if int(choose)<=0 or int(choose)>len(adminmenu):
                print("Please enter a number between 1 and "+ str(len(adminmenu)))          # protection code for breaking
            else:
                admin_choose=adminmenu[int(choose)-1]
                print("---"+admin_choose+"---")
                if choose==1:
                    Library().list_book()
                elif choose==2:
                    Library.create_example_books(self)
                elif choose==3:                                  #options for admin
                    Library.search_book()
                elif choose==4:
                    Library.update_book_copies()
                elif choose==5:
                    Library.update_book_copies()
                elif choose==6:
                    Library.update_book_copies()
                elif choose==7:
                    UsersDB.list_user(self)
                elif choose==8:
                    UsersDB.add_user(self)
                elif choose==9:
                    UsersDB.remove_user(self)
                elif choose==10:
                    break

        
        pass

    def show_student_menu(self):
        """ This method shows the student menu and do redirection """
        #  TODO: implement the method to welcome the student and show the admin menu by using current_user value and do
        #   the redirection to the methods according to the choice with the required implementations
        # write your code below
        print("Dear "+str(self.current_user)+", Welcome to student menu")       #Welcome the user 
        Student().__init__()
        usermenu=User().student_menu                #user interface
        while self.choose_action==True:
            choose=int(input("Your choose = "))
            if int(choose)<=0 or int(choose)>len(usermenu):
                print("Please enter a number between 1 and "+str(len(usermenu)))
            else:
                user_choose=usermenu[int(choose)-1]
                print("---"+user_choose+"---")              # options for user
                if choose==1:
                    Library.search_book(self)
                elif choose==2:
                    Book().display()
                    bid=input("What is the id of a book that you want to borrow?:")
                    Library().add_book()
                elif choose==3:
                    Book().display()
                    bid=input("Which book is you want to delete?:")
                    Library().remove_book(self,bid)
                elif choose==4:
                    Library.update_book_copies(self)
                elif choose==5:
                    break

        pass


if __name__ == '__main__':
    main = Main()           # Main code which is neccesary for running our script

    main.login()              #after main we will  be log in
