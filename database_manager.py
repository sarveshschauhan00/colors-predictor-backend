import mysql.connector

# Replace these values with your actual MySQL server details
host = "localhost"
port = 3306
user = "root"
password = "12345678"
database = "mydatabase"

try:
    # Establish a connection
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    # If the connection is successful, print a success message
    print("Connected to the MySQL database!")

    # Create a cursor
    cursor = connection.cursor()

    # Example query: Select all records from a hypothetical 'users' table
    query = "SELECT * FROM users;"
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

except mysql.connector.Error as err:
    # Handle any errors that occurred during the connection or query execution
    print(f"Error: {err}")

finally:
    # Close the cursor and connection in the finally block to ensure they're always closed
    if 'cursor' in locals() and cursor.is_open():
        cursor.close()
        print("Cursor closed.")
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")
