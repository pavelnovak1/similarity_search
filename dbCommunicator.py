import psycopg2 as db


class DBCommunicator:

    def __init__(self):
        self.connection = db.connect("dbname=host_behavior user=postgres password=gynemi4jov")
        self.cursor = self.connection.cursor()
        self.connected = True

    def dbclose(self):
        if self.connection is not None:
            self.connection.close()

    def dbexecute(self, command):
        if self.connected:
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            return result
        return None
