import mysql.connector as mysql


class MySQLConnection:
    """
    A module to ease in the connection with mysql database and update data.
    The
    """

    def __init__(self, host="localhost", user="python", passwd="python", ):
        self.__CONNECTOR = mysql.connect(
            host=host, user=user, passwd=passwd, charset="utf8")
        self.__ADMIN = self.__CONNECTOR.cursor()

    def create_new_database(self, database_name: str) -> bool:
        """
        Create a database with the specified name.
        @param database_name: Name of the database to create.
        @return: True if successful, False otherwise.
        """
        self.__ADMIN.execute("CREATE DATABASE %s" % database_name)
        return True

    def create_new_table(self, database_name: str, table_name: str, contents: dict) -> bool:
        """
        Creates a new table to the given database
        @param database_name: The database holding the table
        @param table_name: The name of the table to be created
        @param contents: Dictionary containing the name of the columns as key and their respective datatype as values.
        Look at the default mysql datatype for more information.
        @return: True if successful, False otherwise.
        """
        self.__ADMIN.execute("CREATE TABLE %s" % table_name)
        return True


MySQLConnection().create_new_database("Test")
