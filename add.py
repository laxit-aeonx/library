import mysql.connector
from datetime import datetime

# Take inputs from users
name = input("Enter the book's name: ")
author = input("Enter the author's name: ")
issued = input("Enter the issued date (YYYY-MM-DD): ")
deposited = input("Enter the deposited date (YYYY-MM-DD): ")

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="",
    database="library"
)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# SQL query to insert data into the 'books' table
insert_query = """
INSERT INTO books (name, author, issued, deposited) 
VALUES (%s, %s, %s, %s)
"""

# Execute the SQL query to insert data into the 'books' table
cursor.execute(insert_query, (name, author, issued, deposited))

# Commit the changes and close the connection
connection.commit()
connection.close()
