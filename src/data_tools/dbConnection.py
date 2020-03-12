import psycopg2 as db

"""
This class is for direct communication to database. Includes creating connection to database and executing arbitrary SQL command
"""


class dbConnection:

    def __init__(self):
        self.connection = db.connect("dbname=host_behavior user=postgres password=gynemi4jov")
        self.cursor = self.connection.cursor()

    def dbclose(self):
        """
        Close connection to database
        :return: Nothing
        """
        self.connection.close()

    def dbGetData(self, command):
        """
        Executes the specified SQL command
        :param command: command
        :return: Command result, None if database is not connected
        """
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        return result

    def dbInsertData(self, command):
        """
        Executes Insert commands
        :param command : command
        :return 
        """
        self.cursor.execute(command)
        self.connection.commit()
