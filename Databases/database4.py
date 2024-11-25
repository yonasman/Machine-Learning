import sqlite3
import json
# connect to sqlite
conn = sqlite3.connect('manytomany.sqlite')
# initialize a cursor object
cursor = conn.cursor()
# execute queries
cursor.executescript(
    '''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;
    
    CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
    );

    CREATE TABLE Course (
        id     INTEGER PRIMARY KEY,
        title  TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id     INTEGER,
        course_id   INTEGER,
        role        INTEGER,
        PRIMARY KEY (user_id, course_id)
    )
    '''
)

# read the the json file
def read_and_insert():
    fileName = input("Enter the file name: ")
    with open(fileName) as file:
        data = file.read()
        json_data = json.loads(data)
        
        for entry in json_data:
            name = entry[0]
            title = entry[1]
            role = entry[2]
            # print(name, title,role)
            
            # insert the data into tables
            # insert into user table
            cursor.execute(
                '''
                INSERT OR IGNORE INTO User(name) VALUES(?)
                ''',(name,)
            )
            # grab the user_id
            cursor.execute("SELECT id FROM User WHERE name = ? ",(name,))
            user_id = cursor.fetchone()[0]
            # insert into course table
            cursor.execute(
                '''
                INSERT OR IGNORE INTO Course(title) VALUES(?)
                ''',(title,)
            )
            # grab the course_id
            cursor.execute("SELECT * FROM Course WHERE title = ? ", (title,))
            course_id = cursor.fetchone()[0]
            # insert into member table
            cursor.execute('''INSERT OR REPLACE INTO Member(user_id,course_id,role)
                        VALUES(?,?,?)''',(user_id,course_id,role))
        # commit to the db
        conn.commit()
read_and_insert()
