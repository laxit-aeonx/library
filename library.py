import mysql.connector
from tabulate import tabulate

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

# Execute the SQL query to select all data from the 'books' table
cursor.execute("SELECT * FROM books")

# Fetch all the data from the 'books' table
data = cursor.fetchall()

# Display data in a table
table_data = [list(row) for row in data]
headers = [desc[0] for desc in cursor.description]
print(tabulate(table_data, headers, tablefmt="grid"))

# Close the connection
connection.close()
