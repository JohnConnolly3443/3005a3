import psycopg2 #database adaptor

hostname = 'localhost'
database = 'a3'
username = 'postgres'
pwd = '1' #i set pgadmin4's password to 1
port_id = '5432'


conn = psycopg2.connect( #connection to the database
    host = hostname, 
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
    )
    
cur = conn.cursor() #cursor is an object used to query the database

def getAllStudents():
    cur.execute("SELECT * FROM students")
    print(cur.fetchall()) #read the results from the previous query

def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)", (first_name, last_name, email, enrollment_date)) 
    conn.commit() #commits it to database, without this its not actually represented
    getAllStudents()

def updateStudentEmail(student_id, new_email):
    cur.execute("UPDATE students SET email = %s WHERE STUDENT_ID = %s", (new_email, student_id))
    conn.commit()

def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE STUDENT_ID = %s", (student_id,))
    conn.commit()

while True: 
    print("(1) to get all students") #asks user which function to use
    print("(2) to add student")
    print("(3) to update student email")
    print("(4) to delete student")
    choice = int(input("(-1) to exit: "))
    if (choice == 1):
        getAllStudents()
        print()
        continue
    if (choice == 2):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        enrollment_date = input("Enrollment date (xxxx-mm-dd): ")
        addStudent(first_name,last_name,email,enrollment_date)
        print()
        continue
    if (choice == 3):
        student_id = input("student id: ") #not int(input()) cause it expects a string 
        email = input("student email: ")
        updateStudentEmail(student_id, email)
        print()
        continue
    if (choice == 4):
        student_id = int(input("student id: "))
        deleteStudent(student_id)
        print()
        continue
    if (choice == -1):
        break
    
    
conn.close() #closes the connection to the database

