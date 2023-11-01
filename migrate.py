import mysql.connector

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

# SQL query to create a 'books' table
create_table_query = """
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    issued DATE,
    deposited DATE
)
"""

# Execute the SQL query to create the table
cursor.execute(create_table_query)

# Commit the changes and close the connection
connection.commit()
connection.close()
