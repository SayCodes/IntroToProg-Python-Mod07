# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sayali Bhosale,02/25/2024,Classes and Objects
# ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError

# Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
"""
FILE_NAME = "Enrollments.json"

# Variables
menu_choice: str = ""
students: list = []


class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a JSON file into a list."""
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except FileNotFoundError as e:
            IO.output_error_messages("File not found.", e)
        except JSONDecodeError as e:
            IO.output_error_messages("File not in json format.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes to a JSON file."""
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file)
        except IOError as e:
            IO.output_error_messages("Error, cannot write.", e)


class IO:
    """Input/output operations."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        if error:
            print(f"Error: {message} {error}")
        else:
            print(f"Error: {message}")

    @staticmethod
    def output_menu(menu):
        print(menu)

    @staticmethod
    def input_menu_choice():
        """User input for menu choice."""
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data):
        """Outputs student data."""
        for student in student_data:
            print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")

    @staticmethod
    def input_student_data(student_data: list):
        """User input for student data."""
        try:
            first_name = input("Enter student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should only contain letters.")
            last_name = input("Enter student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should only contain letters.")
            course_name = input("Enter course name: ")
            student_data.append({"FirstName": first_name, "LastName": last_name, "CourseName": course_name})
            print("Student registered successfully.")
        except ValueError as e:
            IO.output_error_messages(str(e))


class Person:
    """A person with a first and last name."""

    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("The first name should only contain letters.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("The last name should only contain letters.")
        self._last_name = value


class Student(Person):
    """A student with a first name, a last name, and a course."""

    def __init__(self, first_name="", last_name="", course=""):
        super().__init__(first_name, last_name)
        self.course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value


FileProcessor.read_data_from_file(FILE_NAME, students)

# Main loop
while menu_choice != "4":
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)

    elif menu_choice == "2":
        IO.output_student_courses(students)

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        print("Data saved successfully to file.")

    elif menu_choice == "4":
        print("Program Ended\n")

    else:
        IO.output_error_messages("Please select option 1, 2, 3 or 4.")
