# Python_Dept-Instructor_Sqlite

 
This Python code defines a simple command-line interface (CLI) for managing a university database. Here's what it does:

Database Setup: It establishes a SQLite database named university.db with two tables: department and instructor. The department table contains columns for name, location, and budget, while the instructor table contains columns for ID, name, and department. The department column in the instructor table is a foreign key referencing the name column in the department table.

Function Definitions:

instructorSearch(): Prompts the user to input an instructor ID, then searches the instructor table for that ID. If found, it prints the instructor's name, department, and calls the locationSearch() function to find and print the department's location.

locationSearch(departmentName): Takes a department name as input, searches the department table for that department, and prints its location.

departmentSearch(): Prompts the user to input a department name, then searches the department table for that name. If found, it prints the department's location, budget, and the names of instructors in that department.

addInstructor(): Guides the user through adding a new instructor to the database, ensuring the uniqueness of the instructor ID and checking if the department exists before insertion.

addDepartment(): Guides the user through adding a new department to the database, ensuring the uniqueness of the department name.

showAll(): Prints all the records from both the department and instructor tables.

main(): The main function of the program. It creates the database tables if they don't exist and presents a menu to the user for interacting with the database. The user can choose options to search for instructors or departments, add new instructors or departments, display all records, or exit the program.

Main Execution:
It starts by creating the database tables if they don't exist.
Then, it enters a loop where it displays a menu to the user, takes their input, and performs the corresponding action until the user chooses to exit the program.
Overall, this code provides a basic interface for managing a simple university database, allowing users to add, search, and display information about departments and instructors.
