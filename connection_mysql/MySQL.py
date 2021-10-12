import mysql.connector as mysql


class MySQLConnection:
    """
    A module to ease in the connection with mysql database and update data.
    The
    """

    def __init__(self, host="localhost", user="python", passwd="python", database="bank"):
        self.__DATABASE = database
        self.__CONNECTOR = mysql.connect(
            host=host, user=user, passwd=passwd, charset="utf8", database=database)
        self.__ADMIN = self.__CONNECTOR.cursor()

    def test(self):
        return self.__ADMIN
