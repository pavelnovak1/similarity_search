import psycopg2 as db

"""
This class is used to establish a connection and to communicate with the PostgreSQL database.
"""


class db_connection:

    def __init__(self):
        """
        Establish the connection to the database.
        """
        self.connection = db.connect("dbname=db_host_profiles user=postgres password=gynemi4jov")
        self.cursor = self.connection.cursor()

    def get_data(self, command):
        """
        Executes the specified SQL command which returns some data.
        :param command: command
        :return: Command result.
        """
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        return result

    def insert_data(self, command):
        """
        Executes the specified SQL command which does not return any data.
        :param command : command
        :return 
        """
        self.cursor.execute(command)
        self.connection.commit()
