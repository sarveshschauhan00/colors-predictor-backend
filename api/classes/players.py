import mysql.connector
from connection_main import connection

class Player:
    def __init__(self, user_name, password, balance) -> None:
        self.user_name = user_name
        self.password = password
        self.balance = balance
        self.cursor = connection.cursor()

        

    def fetch_player_info(self):
        connect = self.connect
        query = "SELECT * FROM users;"
        self.cursor.execute(query)
        
    def readData(self):
        # Fetch all the results
        results = self.cursor.fetchall()

        # Print the results
        for row in results:
            print(row)