import sqlite3
from sqlite3 import Error

class database:
    """Main database class that controls all the functionality for input /
        out of the database."""


    def __init__(self):
        self.conn = None


    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        self.conn = conn


    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_chromosome(self, chromosome):
        """
        Create a new task
        :param conn:
        :param chromosome:
        :return:
        """

        sql = ''' INSERT INTO data(generation,fitness,chromosome)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, chromosome)
        self.conn.commit()
        return cur.lastrowid

    def create_data_table(self, ga):

        # create a database connection
        self.conn = self.create_connection(ga.database_name)

        # create tables
        if self.conn is not None:
            # create projects table
            self.create_table(ga.sql_create_data_structure)

            # create tasks table
            # create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")

        with self.conn:

            # Create a fake chromosome
            # Generation / Fitness / chromosome
            data1 = (0, 99, '[gene,gene,gene,gene]')
            data2 = (1, 200, '[gene,gene,gene,gene]')
            # Add chromosome to the data table inside the database
            self.insert_chromosome(data1)
            self.insert_chromosome(data2)
