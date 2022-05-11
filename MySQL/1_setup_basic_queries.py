# MySQL Database.
# Structure Queries Language.
# MySQL Database is one of the Most Popular Database.
# SQL is a required Skill. 
# MySQL is Designed to Run on a Server.

import mysql.connector

db = mysql.connector.connect (
      host='localhost',
      user='thor',
      passwd = 'Thor561111',
      database = 'TestDatabase' # made after -> mycursor.execute("CREATE DATABASE TestDatabase") # First query we make will create the database
)

mycursor = db.cursor()

# First query we make will create the database
#mycursor.execute("CREATE DATABASE TestDatabase")

#mycursor.execute("CREATE TABLE Person (name VARCHAR(255), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

