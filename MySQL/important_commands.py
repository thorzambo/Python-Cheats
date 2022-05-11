import mysql.connector
from datetime import datetime
# -----------------------------------------------
''' SETUP AND BASIC QUERIES'''
# -----------------------------------------------

# MySQL Database.
# Structure Queries Language.
# MySQL Database is one of the Most Popular Database.
# SQL is a required Skill. 
# MySQL is Designed to Run on a Server.

db = mysql.connector.connect (
      host='localhost',
      user='thor',
      passwd = 'Thor561111',
      database = 'TestDatabase' # made after -> mycursor.execute("CREATE DATABASE TestDatabase") # First query we make will create the database
)

mycursor = db.cursor()


# -----------------------------------------------
''' CREATING TABLES. INSERTING AND SELECTING '''
# -----------------------------------------------


# First query we make will create the database
#mycursor.execute("CREATE DATABASE TestDatabase")

#mycursor.execute("CREATE TABLE Person (name VARCHAR(255), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

''' 
mycursor.execute("DESCRIBE Person")
for x in mycursor:
      print(x)
'''
      
''' 
('name', b'varchar(255)', 'YES', '', None, '')
('age', b'smallint unsigned', 'YES', '', None, '')
('personID', b'int', 'NO', 'PRI', None, 'auto_increment') 
'''

# How to add someone into the Table
#mycursor.execute("INSERT INTO Person(name, age) VALUES (%s, %s)", ("George", 14))
#db.commit()

mycursor.execute("DESCRIBE Person")
for x in mycursor:
      print(x)


# Show Person inside Tables all rows and columns INSIDE THE db. 
mycursor.execute("SELECT * FROM Person")

for x in mycursor:
      print(x) # NOTICE IT OUTPUTS TUPLES

#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Thor", datetime.now(), "O"))
#db.commit()



# -----------------------------------------------
''' SELECTING DATA AND ALTERING TABLES'''
# -----------------------------------------------

'''SELECT From Database a Particular Gender (in this case)'''
#mycursor.execute("SELECT * FROM Test WHERE gender = 'M'")
#mycursor.execute("SELECT * FROM Test WHERE gender = 'F'")
#mycursor.execute("SELECT * FROM Test WHERE gender = 'O'")

# ORDERING:
mycursor.execute("SELECT id, name FROM Test WHERE gender = 'O' ORDER BY id DESC")

for x in mycursor:
      print(x)


# HOW TO MODIFY A TABLE
# Add a Column, Change a Header Name etcetc

#mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL") # add a column

mycursor.execute("DESCRIBE Test")
print(mycursor.fetchone())

for x in mycursor:
      print(x)

# Remove Header FOOD From Table
#mycursor.execute("ALTER TABLE Test DROP Food")

# Change Column Name
#mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(4)")

mycursor.execute("DESCRIBE Test")

for x in mycursor:
      print(x)



# -----------------------------------------------
''' FOREIGN KEYS AND RELATING TABLES '''
# -----------------------------------------------

users = [("Leo", "zambo"),
         ("Thor", "Thorium"),
         ("Lisa", "Prinmcy")]

user_scores = [(69, 67),
               (45,80),
               (99, 32)]

mycursor = db.cursor()

# Create Tables, Parent table and Child table
Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"
Q2 = "CREATE TABLE Scores (userid int PRIMARY KEY, FOREIGN KEY (userid) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

'''
mycursor.execute(Q1)
mycursor.execute(Q2)
'''

mycursor.execute("SHOW TABLES")

for i in mycursor:
      print(i)
      
      
Q3 = "INSERT INTO Users (name, passwd) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (userid,game1,game2) VALUES (%s,%s,%s)"

for x, user in enumerate(users):
      mycursor.execute(Q3, user)
      last_id = mycursor.lastrowid
      mycursor.execute(Q4, (last_id,) + user_scores[x])
   
db.commit()
   
mycursor.execute("SELECT * FROM Users")
for x in mycursor:
      print(x)

mycursor.execute("SELECT * FROM Users")
for x in mycursor:
     print(x)
