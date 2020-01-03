import psycopg2 as db


class DBCommunicator:

    def __init__(self):
        self.connection = db.connect("dbname=host_behavior user=postgres password=gynemi4jov")
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
        Executes the specified command
        :param command: command
        :return: Command result, None if database is not connected
        """
        if self.connected:
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            return result
        return None
