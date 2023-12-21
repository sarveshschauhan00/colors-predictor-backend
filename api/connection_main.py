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

    # Your SQL query or operations go here

except mysql.connector.Error as err:
    # Handle any errors that occurred during the connection attempt
    print(f"Error: {err}")

finally:
    # Close the connection in the finally block to ensure it's always closed
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")


