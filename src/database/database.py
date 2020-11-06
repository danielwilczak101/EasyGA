import sqlite3
from sqlite3 import Error
import os


class database:
    """Main database class that controls all the functionality for input /
    out of the database."""


    def __init__(self):
        self.conn = None


    def create_connection(self, db_file):
        """Create a database connection to the SQLite database
         specified by db_file."""

        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        self.conn = conn


    def create_table(self, create_table_sql):
        """Create a table from the create_table_sql statement."""

        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_chromosome(self, generation, chromosome):
        """ """

        # Structure the insert data
        db_chromosome = (generation, chromosome.fitness, '[chromosome]')

        # Create sql query structure
        sql = ''' INSERT INTO data(generation,fitness,chromosome)
         VALUES(?,?,?) '''

        cur = self.conn.cursor()
        cur.execute(sql, db_chromosome)
        self.conn.commit()
        return cur.lastrowid

    def insert_current_population(self, ga):
        """ Insert current generations population """

        # For each chromosome in the population
        for chromosome in ga.population.chromosome_list:
            # Insert the chromosome into the database
            self.insert_chromosome(ga.current_generation, chromosome)


    def create_data_table(self, ga):
        """Create the data table that store generation data."""

        try:
            # Remove old database file if it exists.
            os.remove(ga.database_name)
        except:
            # If the database does not exist continue
            pass

        # create a database connection
        self.conn = self.create_connection(ga.database_name)

        # create tables
        if self.conn is not None:
            # create projects table
            self.create_table(ga.sql_create_data_structure)

        else:
            print("Error! cannot create the database connection.")


    def query_all(self, query):
        """Query for muliple rows of data"""

        cur = self.conn.cursor()
        cur.execute(query)

        return cur.fetchall()

    def query_one_item(self, query):
        """Query for single data point"""

        cur = self.conn.cursor()
        cur.execute(query)
        query_data = cur.fetchone()

        return query_data[0]
