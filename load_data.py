import json #The file type of this project is in JSON format
from dotenv import load_dotenv #to load the encrypted password created for the database
import os #This is important because I set the sql_database from the command prompt
import mysql.connector

load_dotenv() 
conn =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv("sql_database_pwd"),
    database = "students_rooms"
)

print("Connected successfully")
cursor=  conn.cursor()

#Load the JSON dataset rooms

with open ("rooms.json") as f:
    rooms = json.load(f)

for room in rooms:
    cursor.execute(
        "INSERT IGNORE INTO rooms (id, name) VALUES (%s, %s)",
        (room["id"], room["name"])
    )

#Load the JSON dataset students
with open ("students.json") as f:
    students = json.load(f)

for student in students:
    cursor.execute(
        """INSERT IGNORE INTO students (birthday, id, name, room, sex)
        VALUES (%s, %s, %s, %s, %s)""",
        (
            student["birthday"],
            student["id"],
            student["name"],
            student["room"],
            student["sex"],
        )

    )

    conn.commit()
    #cursor.close()
    #conn.close()

    print("Data successfully loaded")



