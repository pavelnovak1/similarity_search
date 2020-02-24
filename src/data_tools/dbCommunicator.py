import psycopg2 as db

"""
This class is for direct communication to database. Includes creating connection to database and executing arbitrary SQL command
"""
class DBCommunicator:

    def __init__(self):
        self.connection = db.connect("dbname=host_behavior user=postgres")
        self.cursor = self.connection.cursor()
        self.connected = True

    def dbclose(self):
        """
        Close connection to database
        :return: Nothing
        """
        if self.connection is not None:
            self.connection.close()

    def dbexecute(self, command):
        """
        Executes the specified SQL command
        :param command: command
        :return: Command result, None if database is not connected
        """
        if self.connected:
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            return result
        return None

    
    def dbExecuteNoResult(self, command):
        """
        Executes command where output is no data but only changes in database
        :param command : command
        :return 
        """
        self.cursor.execute(command)
        self.connection.commit()
