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
        self.menu_items=["Listbooks","Createabook","Deleteabook","Searchforabook",
"Change number of a copies of a book", "Show students borrowed a book by ""ID",
"List Users", "Create User","Delete User", "Exit"]

        pass

    def display(self):
        """ This method displays item menu """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below
        for i in len(self.menu_items):
        print(self.menu_items)
        pass


class Menu:
    """ This class initialises a menu """

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below

        pass

    def display(self):
        """ This method displays menu instance """
        #  TODO: implement the method to print the menu items here with the header according to the flag
        # write your code below
        pass

    def add_menu_item(self):
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
        pass

    def display(self):
        """ This method displays user instance """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below
        pass

    def menu_builder(self):
        """ This method build the default menus for admin and student """
        # TODO: implement the method to build the menu here by using the class level attribute "menu" and its method
        #  "add_menu_item" write your code below
        pass


class Admin:
    #  TODO: inherit the user class
    #  TODO: initialise the class level attributes here
    # write your code below
    pass

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        pass


class Student:
    #  TODO: inherit the user class
    #  TODO: initialise the class level attributes here
    # write your code below
    pass

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        pass


class UsersDB:
    """ This class initialises the the DB for user instances """
    #  TODO: initialise the class level attributes here
    # write your code below
    pass

    def __init__(self):
        #  TODO: implement the method to call the "create_example_users" function here according to the flag
        # write your code below
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
        pass

    def remove_user(self):
        """ This method removes a user from users DB """
        #  TODO: implement the method to remove a user by the name after listing all the users by "list_user" function
        # write your code below
        pass

    def list_user(self):
        """ This method list all users in the users db """
        # TODO: implement the method to list all student users and return a string that shows it has been added
        #  successfully write your code below
        # write your code below
        pass

    def validate_user(self):
        """ This method validate user credentials """
        # TODO: implement the method to check username and password and return the username in terms of correct
        #  credentials and False in terms of wrong credentials
        # write your code below
        pass


class Book:
    """ This class initialises the book instances """

    def __init__(self):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below
        pass

    def display(self):
        """ This method displays book instances """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below
        pass


class Library:
    """ This class initialises the library system """
    #  TODO: initialise the class level attributes here
    # write your code below
    pass

    def __init__(self):
        #  TODO: implement the method to call the function "create_example_books" according to the flag
        # write your code below
        pass

    def create_example_books(self):
        """ This method creates example books to be used """
        # TODO: implement the method to create the example books by using "add_book" function and return a string
        #  that shows it has been created successfully
        # write your code below
        pass

    def add_book(self):
        """ This method adds book to the library """
        # TODO: implement the method to add book by creating Book class object and to add it to the class level
        #  attribute "book_objects" and return a string that shows it has been added successfully
        # write your code below
        pass

    def remove_book(self):
        """ This method removes book from the library """
        # TODO: implement the method to remove book by its id after listing all the books by list_book function (dont
        #  forget to remove it from the author to books list) and return a string shows the status (deleted/not found)
        # write your code below
        pass

    def list_book(self):
        """ This method lists all the library in the library """
        # TODO: implement the method to list all books and return a string shows that all books have been listed
        # write your code below
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
        pass

    def login(self):
        """ This method deals with the login process """
        # TODO: implement the method to deal with the login attempts by using validate_user function from userDB
        #  instance and printing the required messages. In terms of success attempt, the method should call
        #  show_student_menu or show_admin_menu
        # write your code below
        pass

    def show_admin_menu(self):
        """ This method shows the admin menu and do redirection """
        #  TODO: implement the method to welcome the admin and show the admin menu by using current_user value and do
        #   the redirection to the methods according to the choice with the required implementations
        # write your code below
        pass

    def show_student_menu(self):
        """ This method shows the student menu and do redirection """
        #  TODO: implement the method to welcome the student and show the admin menu by using current_user value and do
        #   the redirection to the methods according to the choice with the required implementations
        # write your code below
        pass


if __name__ == '__main__':
    main = Main()
    main.login()
