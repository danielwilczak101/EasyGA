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
        self._database_name = 'database.db'


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


    def create_connection(self):
        """Create a database connection to the SQLite database
         specified by db_file."""

        conn = None
        try:
            conn = sqlite3.connect(self.database_name)
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
        self.conn = self.create_connection()

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


    def past_runs(self):
        """Show a summerization of the past runs that the user has done."""

        query_data = self.query_all(f"SELECT id,generation_goal,chromosome_length FROM config;")

        print(query_data)


    def get_most_recent_config_id(self):
        """Function to get the most recent config_id from the database."""

        query_data = self.query_one_item("SELECT max(config_id) FROM config")

        return query_data

    def default_config_id(method):
        """Decorator used to set the default config_id"""
        def new_method(self, config_id = None):
            input_id = self.config_id if config_id is None else config_id
            return method(self, input_id)
        return new_method


    @default_config_id
    def get_generation_total_fitness(self,config_id):
        """Get each generations total fitness sum from the database """

        query_data = self.query_all(f"SELECT SUM(fitness) FROM data WHERE config_id={config_id} GROUP BY generation;")

        return self.formated_query_data(query_data);


    @default_config_id
    def get_total_generations(self,config_id):
        """Get the total generations from the database"""

        query_data = self.query_one_item(f"SELECT COUNT(DISTINCT generation) FROM data WHERE config_id={config_id};")

        return query_data


    @default_config_id
    def get_highest_chromosome(self,config_id):
        """Get the highest fitness of each generation"""

        query_data = self.query_all(f"SELECT fitness, max(fitness) FROM data WHERE config_id={config_id} GROUP by generation;")

        return self.formated_query_data(query_data);


    @default_config_id
    def get_lowest_chromosome(self,config_id):
        """Get the lowest fitness of each generation"""

        query_data = self.query_all(f"SELECT fitness, min(fitness) FROM data WHERE config_id={config_id} GROUP by generation;")

        return self.formated_query_data(query_data);


    def formated_query_data(self,query_data):
        """Format the query data so its in a proper list"""

        formated_query_data = [i[0] for i in query_data]

        return formated_query_data;


    @property
    def database_name(self):
        return self._database_name


    @database_name.setter
    def database_name(self, value_input):
        raise Exception("Invalid usage, please use ga.database_name instead.")


    @property
    def conn(self):
        """Getter function for conn"""
        # Return if the connection has already been set
        if self._conn is not None:
            return self._conn

        else:
            # If the connection has not been set yet
            try:
                # Check if you can connect to the database
                self._conn = self.create_connection()
            except:
                # if the connection doesnt exist then print error
                raise Exception("""You are required to run a ga before you
                 can connect to the database. Run ga.evolve() or ga.active()""")


    @conn.setter
    def conn(self, value_input):
        """Setter function for conn"""

        # Set the name in the ga attribute
        self._conn = value_input

    @property
    def config_id(self):
      """Getter function for config_id"""
      # Return if the config_id has already been set
      if self._config_id is not None:
          return self._config_id

      else:
          # If the config_id has not been set yet
          try:
              # Check if you can connect to the database
              self._config_id = self.get_most_recent_config_id()
          except:
              # if the config_id doesnt exist then print error
              raise Exception("""You are required to run a ga before you
               can connect to the database. Run ga.evolve() or ga.active()""")


    @config_id.setter
    def config_id(self, value_input):
      """Setter function for config_id"""

      # Set the name in the ga attribute
      self._config_id = value_input
