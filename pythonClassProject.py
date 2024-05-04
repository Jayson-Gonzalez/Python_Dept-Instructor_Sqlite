import sqlite3

def instructorSearch():
    
    instructorID = input("Enter the instructor ID:")
    
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM instructor WHERE id=?",(instructorID,))
    instructor = cur.fetchone()
    conn.close()
    
    if instructor:
        print(f"Name:{instructor[1]}")
        print(f"Department:{instructor[2]}")
        locationSearch(instructor[2])
    else:
        print("ID not in the database")
        
def locationSearch(departmentName):
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()
    cur.execute("SELECT location FROM department WHERE name=?",(departmentName,))
    location = cur.fetchone()
    if location:
        print(f"Department Location:{location[0]}")
    conn.close()

def departmentSearch():
    departmentName = input("Enter the department name:").lower()  
    
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM department")
    departments = cur.fetchall()
    flag = False
    
    for i in departments:
        if departmentName == i[0].lower(): 
            flag = True
            
            print(f"Location:{i[1]}")
            print(f"Budget:{i[2]}")
            print("Instructors:")
            
            cur.execute("SELECT name FROM instructor WHERE department=?",(i[0],))
            instructors = cur.fetchall()
            instructors = ', '.join([instructor[0] for instructor in instructors])

            print(instructors)
            
            break
    if not flag:
        print("The department name does not appear in the database")
    
    conn.close()

def addInstructor():
    while True:
        instructorID = input("Enter the instructor id,must be number:")
        
        if not instructorID.isdigit():
            print("Error: Instructor ID must be a number.")
        else:
            break
    
    instructorName = input("Enter the instructor name:")
    departmentName = input("Enter the department name:").upper()
    
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM department WHERE name=?",(departmentName,))
    department = cur.fetchone()
    
    if department:
        cur.execute("SELECT * FROM instructor WHERE id=?",(instructorID,))
        existingInstructor = cur.fetchone()
        
        if not existingInstructor:
            cur.execute("INSERT INTO instructor VALUES (?, ?, ?)",(instructorID, instructorName, departmentName))
            conn.commit()
            print("New instructor added successfully")
        else:
            print("Instructor id already exists")
            
    else:
        print("The department does not exist and hence the instructor record cannot be added to the database.")
    conn.close()

def addDepartment():
    departmentName = input("Enter the department name:").upper()  
    location = input("Enter the location:")
    budget = float(input("Enter the budget:"))
    
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM department WHERE name=?", (departmentName,))
    existingDepartment = cur.fetchone()
    
    if not existingDepartment:
        cur.execute("INSERT INTO department VALUES (?, ?, ?)",
                  (departmentName, location, budget))
        conn.commit()
        print("New department added successfully.")
    else:
        print("Department already exists.")
    
    conn.close()

def showAll():
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()
    
    print("Department Table:")
    
    cur.execute("SELECT * FROM department")
    departments = cur.fetchall()
    
    print("Name\tLocation\tBudget")
    
    for i in departments:
        print(f"{i[0]}\t{i[1]}\t\t{i[2]}")
    
    print("Instructor Table:")
    
    cur.execute("SELECT * FROM instructor")
    instructors = cur.fetchall()
    
    print("ID\tName\t\tDepartment")
    
    for i in instructors:
        print(f"{i[0]}\t{i[1]}\t{i[2]}")
    
    conn.close()
    
def main():
    
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS department
                                   (name TEXT PRIMARY KEY, 
                                    location TEXT, 
                                    budget REAL)''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS instructor
                               (id INTEGER PRIMARY KEY, 
                               name TEXT, 
                               department TEXT,
                               FOREIGN KEY (department) 
                               REFERENCES department(name))''')
    conn.commit()
    conn.close()

    while True:
        
        print("Menu:")
        print("1. Find instructor information")
        print("2. Find department information")
        print("3. Add a new instructor")
        print("4. Add a new department")
        print("5. Show tables")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        print()
        
        if choice == "1":
            instructorSearch()
            print()
        elif choice == "2":
            departmentSearch()
            print()
        elif choice == "3":
            addInstructor()
            print()
        elif choice == "4":
            addDepartment()
            print()
        elif choice == "5":
            showAll()
            print()
        elif choice == "6":
            break
        else:
            print("Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
