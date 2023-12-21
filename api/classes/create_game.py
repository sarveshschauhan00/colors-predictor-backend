import mysql.connector

# Replace these values with your actual MySQL server details
host = "localhost"
port = 3306
user = "root"
password = "12345678"
database = "games"
period = 12356

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

def create_game_table(period):
    try:
        create_table = f"CREATE TABLE {period} ( id INT AUTO_INCREMENT PRIMARY KEY, userid VARCHAR(50) NOT NULL, bet_count int NOT NULL, bet_amount INT, number INT );"

    except mysql.connector.Error as err:
        # Handle any errors that occurred during the connection attempt
        print(f"Error: {err}")

    finally:
        # Close the connection in the finally block to ensure it's always closed
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed.")


