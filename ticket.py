import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "numeratethenerds@2002",
    database = "mydb1"
) 

conn = db.cursor()

conn.execute("""CREATE TABLE if not exists studentData(
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(50),
    sem INT,
    Degree VARCHAR(10),
    Branch VARCHAR(10),
    GPA INT
    )""")

def create():
    N=int(input("Enter the number of student's details to be entered: "))
    for i in range(N):
        id=int(input("Enter the id of the student: "))
        name=str(input("Enter the name of the student: "))
        sem=int(input("Enter the sem of the student: " ))
        Degree=str(input("Enter the graduation of the student: "))
        Branch=str(input("Enter the branch of the student: "))
        GPA=float(input("Enter the SGPA of the student: "))
        conn.execute("INSERT INTO studentData(id, name, sem, Degree, Branch, GPA) VALUES(%s, %s, %s, %s, %s, %s)", (id, name, sem, Degree,Branch, GPA))
        db.commit()
    
def read():
    conn.execute("SELECT * FROM studentData ORDER BY id ASC")
    for x in conn:
        print(x)

def update():
    old=int(input("Enter the original id of the student: "))
    new=str(input("Enter the new name of the student: "))
    conn.execute("UPDATE studentData SET name = %s WHERE id = %s", (new, old))
    db.commit()
    read()
        
def delete():
    x=input("Enter the id of the student whose record has to deleted: ")
    conn.execute("DELETE FROM studentData WHERE id =%s" %(x))
    db.commit()
    read()
        
operation_dict = {1: create, 2: read, 3: update, 4: delete}

while(True):
    operation = int(input("""To perform the following operations: 
          Press 1 to enter new values:
          Press 2 to view the table: 
          Press 3 to update the records: 
          Press 4 to delete a record: """))
    performing = operation_dict[operation]() 
        


    