import sqlite3
from sqlite3 import Error
import os


class SQL_Database:
    """Main database class that controls all the functionality for input /
    out of the database using SQLite3."""

    sql_type_list = [int, float, str]

    def __init__(self):
        self.conn = None
        self.config_id = None


    def get_current_config(self):
        """Get the current config_id from the config table."""
        return self.query_one_item("SELECT MAX(id) FROM config")


    def sql_type_of(self, obj):
        """Returns the sql type for the object"""

        if type(obj) == int:
            return 'INT'
        elif type(obj) == float:
            return 'REAL'
        else:
            return 'TEXT'


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
        """ Insert one chromosome into the database"""

        # Structure the insert data
        db_chromosome = (self.config_id,generation, chromosome.fitness, repr(chromosome))

        # Create sql query structure
        sql = ''' INSERT INTO data(config_id, generation, fitness, chromosome)
         VALUES(?,?,?,?) '''

        cur = self.conn.cursor()
        cur.execute(sql, db_chromosome)
        self.conn.commit()
        return cur.lastrowid


    def insert_current_population(self, ga):
        """ Insert current generations population """

        # Structure the insert data
        db_chromosome_list = [
        (
        self.config_id,
        ga.current_generation,
        chromosome.fitness,
        repr(chromosome)
        )
         for chromosome in ga.population.get_chromosome_list()
        ]

        # Create sql query structure
        sql = ''' INSERT INTO data(config_id,generation,fitness,chromosome)
         VALUES(?,?,?,?) '''

        cur = self.conn.cursor()
        cur.executemany(sql, db_chromosome_list)
        self.conn.commit()
        return cur.lastrowid


    def get_var_names(self, ga):
        """Returns a list of the names of attributes of the ga."""

        var_names = list(ga.__dict__.keys())

        # Remove leading underscores
        for i in range(len(var_names)):
            if var_names[i][0] == '_':
                var_names[i] = var_names[i][1:]

        return var_names


    def create_all_tables(self, ga):
        """Create the database if it doenst exist and then the data and config
        tables."""

        try:
            # if the database file already exists.
            self.config = self.get_current_config()
        except:
            # If the database does not exist continue
            pass

        # Create the database connection
        self.conn = self.create_connection(ga.database_name)

        if self.conn is not None:
            # Create data table
            self.create_table(ga.sql_create_data_structure)
            # Creare config table
            self.create_table(self.create_config_table_string(ga))
        else:
            print("Error! cannot create the database connection.")


    def create_config_table_string(self,ga):
        """Automate the table creation sql statement so that it takes all the
        attribute variables and adds them as columns in the database table config"""

        # Retrieve variable names and assign sql data types
        var_names = self.get_var_names(ga)
        for i in range(len(var_names)):
            var_names[i] += ' ' + self.sql_type_of(var_names[i])

        # Structure the config table
        sql = "CREATE TABLE IF NOT EXISTS config (\nid INTEGER PRIMARY KEY,"
        sql += "\n,".join(var_names)
        sql += "); "

        return sql


    def insert_config(self,ga):
        """Insert the configuration attributes into the config."""

        # Structure the insert data
        db_config_list = list(ga.__dict__.values())

        # Clean up so the sqlite database accepts the data structure
        for i in range(len(db_config_list)):
            if callable(db_config_list[i]):
                db_config_list[i] = db_config_list[i].__name__
            elif type(db_config_list[i]) not in self.sql_type_list:
                db_config_list[i] = str(db_config_list[i])

        # Create sql query structure
        sql = "INSERT INTO config ("
        sql += ",\n".join(self.get_var_names(ga))
        sql += ") VALUES("
        sql += ( ",?"*len(db_config_list) )[1:]
        sql += ") "

        # For some reason it has to be in var = array(tuple()) form
        db_config_list = [tuple(db_config_list)]

        # Execute sql query
        cur = self.conn.cursor()
        cur.executemany(sql, db_config_list)
        self.conn.commit()
        self.config_id = self.get_current_config()
        return cur.lastrowid


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


    def past_runs(self,database_name = 'database.db'):
        """Show a summerization of the past runs that the user has done."""

        self.conn = self.create_connection(database_name)
        query_data = self.query_all(f"SELECT id,generation_goal,chromosome_length FROM config;")
        print(query_data)

    def get_generation_total_fitness(self,config_id = None,database_name = 'database.db'):
        """Get each generations total fitness sum from the database """

        if config_id == None: config_id = self.config_id

        self.conn = self.create_connection(database_name)
        query_data = self.query_all(f"SELECT SUM(fitness) FROM data WHERE config_id={config_id} GROUP BY generation;")

        # Format the fitness data into one list
        formated_query_data = [i[0] for i in query_data]

        return formated_query_data


    def get_total_generations(self,config_id = None,database_name = 'database.db'):
        """Get the total generations from the database"""

        if config_id == None: config_id = self.config_id
        self.conn = self.create_connection(database_name)
        query_data = self.query_one_item(f"SELECT COUNT(DISTINCT generation) FROM data WHERE config_id={config_id};")

        return query_data


    def get_highest_chromosome(self,config_id = None,database_name = 'database.db'):
        """Get the highest fitness of each generation"""

        if config_id == None: config_id = self.config_id

        self.conn = self.create_connection(database_name)
        query_data = self.query_all(f"SELECT fitness, max(fitness) FROM data WHERE config_id={config_id} GROUP by generation;")

        # Format the fitness data into one list
        formated_query_data = [i[0] for i in query_data]

        return formated_query_data;


    def get_lowest_chromosome(self,config_id = None,database_name = 'database.db'):
        """Get the lowest fitness of each generation"""

        if config_id == None: config_id = self.config_id

        self.conn = self.create_connection(database_name)
        query_data = self.query_all(f"SELECT fitness, min(fitness) FROM data WHERE config_id={config_id} GROUP by generation;")

        # Format the fitness data into one list
        formated_query_data = [i[0] for i in query_data]

        return formated_query_data;


    # Getters and setter for class
    def get_config_id(self):

        try:
            # return the config id if its already set
            self.config_id = "something"

        except:
            # config_id and config table dont exist: Tell the user
            print("""You are required to run a ga before you
             can connect to the database. Run ga.evolve()""")


    def get_conn(self):
        """Conn """

        try:
            # Return if the connection has already been set
            return self.conn

        except:

            try:
                # Check if you can connect to the database named in ga
                self.conn = self.create_connection(ga.database_name)
                return self.conn

            except:
                # if the connection
                print("""You are required to run a ga before you
                 can connect to the database. Run ga.evolve()""")
                return
