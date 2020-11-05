import sqlite3
from sqlite3 import Error
import os


class database:
    """Main database class that controls all the functionality for input /
        out of the database."""


    def __init__(self):
        self.conn = None


    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
         specified by db_file."""

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

    def insert_chromosome(self, generation, chromosome):
        """
        Insert a new chromosome
        :param conn:
        :param generation:
        :param chromosome:
        :return:
        """

        # Structure the insert data
        db_chromosome = (generation, chromosome.fitness, '[chromosome]')


        sql = ''' INSERT INTO data(generation,fitness,chromosome)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, db_chromosome)
        self.conn.commit()
        return cur.lastrowid

    def insert_current_population(self, ga):
        """ Insert current generations population """

        for chromosome in ga.population.chromosome_list:
            self.insert_chromosome(ga.current_generation, chromosome)


    def create_data_table(self, ga):

        try:
            # Remove old database if there
            os.remove(ga.database_name)
        except:
            pass

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
