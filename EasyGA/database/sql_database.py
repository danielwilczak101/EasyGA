import sqlite3

from tabulate import tabulate

class SQL_Database:
    """Main database class that controls all the functionality for input /
    out of the database using SQLite3."""


    def __init__(self):
        self.conn = None
        self.config_id = None
        self._database_name = 'database.db'
        self.config_structure = f"""
        CREATE TABLE IF NOT EXISTS config (
        config_id INTEGER,
        attribute_name TEXT,
        attribute_value TEXT)"""


    #=====================================#
    # Create Config and Data Table:       #
    #=====================================#

    def create_all_tables(self, ga):
        """Create the database if it doenst exist and then the data and config
        tables."""

        # Create the database connection
        self.create_connection()

        if self.conn is not None:
            # Create data table
            self.create_table(ga.sql_create_data_structure)
            # Creare config table
            self.create_table(self.config_structure)
            # Set the config id
            self.config_id = self.get_current_config()

        else:
            raise Exception("Error! Cannot create the database connection.")



    def insert_config(self,ga):
        """Insert the configuration attributes into the config."""

        # Get the current config and add one for the new config key
        self.config_id = self.get_current_config()

        # Setting the config_id index if there is no file
        if self.config_id == None:
            self.config_id = 0
        else:
            self.config_id = self.config_id + 1

        # Getting all the attributes from the attributes class
        db_config_dict = (
            (attr_name, getattr(ga, attr_name))
            for attr_name
            in ga.__annotations__
            if attr_name != "population"
        )

        # Types supported in the database
        sql_type_list = [int, float, str]

        # Loop through all attributes
        for name, value in db_config_dict:

            # not a function
            if not callable(value):

                # Convert to the right type
                value = str(value)

                if "'" not in value and '"' not in value:

                    # Insert into database
                    self.conn.execute(f"""
                    INSERT INTO config(config_id, attribute_name, attribute_value)
                    VALUES ('{self.config_id}', '{name}','{value}');""")


        self.config_id = self.get_current_config()


    #=====================================#
    # Decorators:                         #
    #=====================================#

    def default_config_id(method):
        """Decorator used to set the default config_id inside other functions."""

        def new_method(self, config_id = None):

            input_id = self.config_id if config_id is None else config_id

            return method(self, input_id)

        return new_method


    def format_query_data(method):
        """Decorator used to format query data"""

        def new_method(self, config_id):
            query = method(self, config_id)

            # Unpack elements if they are lists with only 1 element
            if type(query[0]) in (list, tuple) and len(query[0]) == 1:
                query = [i[0] for i in query]

            # Unpack list if it is a list with only 1 element
            if type(query) in (list, tuple) and len(query) == 1:
                query = query[0]

            return query

        return new_method

    #=====================================#
    # Request information Queries:        #
    #=====================================#


    def get_current_config(self):
        """Get the current config_id from the config table."""
        return self.query_one_item("SELECT MAX(config_id) FROM config")

    def past_runs(self):
        """Show a summerization of the past runs that the user has done."""

        query_data = self.query_all(f"""
        SELECT config_id,attribute_name,attribute_value
        FROM config;""")

        print(
            tabulate(
                query_data,
                headers = [
                    'config_id',
                    'attribute_name',
                    'attribute_value'
                ]
            )
        )


    @default_config_id
    def get_generation_total_fitness(self, config_id):
        """Get each generations total fitness sum from the database """

        return self.query_all(f"""
         SELECT SUM(fitness)
         FROM data
         WHERE config_id={config_id}
         GROUP BY generation;""")


    @default_config_id
    def get_total_generations(self, config_id):
        """Get the total generations from the database"""

        return self.query_one_item(f"""
        SELECT COUNT(DISTINCT generation)
        FROM data
        WHERE config_id={config_id};""")


    @default_config_id
    def get_highest_chromosome(self, config_id):
        """Get the highest fitness of each generation"""

        return self.query_all(f"""
        SELECT max(fitness)
        FROM data
        WHERE config_id={config_id}
        GROUP by generation;""")


    @default_config_id
    def get_lowest_chromosome(self, config_id):
        """Get the lowest fitness of each generation"""

        return self.query_all(f"""
        SELECT min(fitness)
        FROM data
        WHERE config_id={config_id}
        GROUP by generation;""")


    def get_all_config_id(self):
        """Get an array of all the DISTINCT config_id in the database"""

        return self.query_all(f"""
        SELECT DISTINCT config_id
        FROM config;""")

    def get_each_generation_number(self,config_id):
        """Get an array of all the generation numbers"""

        return self.query_all(f"""
        SELECT DISTINCT generation
        FROM data
        WHERE config_id={config_id};""")



    #=====================================#
    # Input information Queries:          #
    #=====================================#


    def insert_chromosome(self, generation, chromosome):
        """ Insert one chromosome into the database"""

        # Structure the insert data
        db_chromosome = (
            self.config_id,
            generation,
            chromosome.fitness,
            repr(chromosome)
        )

        # Create sql query structure
        sql = """INSERT INTO data(config_id, generation, fitness, chromosome)
                 VALUES(?,?,?,?)"""

        cur = self.conn.cursor()
        cur.execute(sql, db_chromosome)
        self.conn.commit()



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
            for chromosome
            in ga.population
        ]

        # Create sql query structure
        sql = """INSERT INTO data(config_id, generation, fitness, chromosome)
                 VALUES(?,?,?,?)"""

        cur = self.conn.cursor()
        cur.executemany(sql, db_chromosome_list)
        self.conn.commit()



    #=====================================#
    # Functions:                          #
    #=====================================#

    def create_connection(self):
        """Create a database connection to the SQLite database
         specified by db_file."""

        try:
            self.conn = sqlite3.connect(self.database_name)
        except Error as e:
            self.conn = None
            print(e)

    def create_table(self, create_table_sql):
        """Create a table from the create_table_sql statement."""

        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)


    @format_query_data
    def query_all(self, query):
        """Query for muliple rows of data"""

        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()


    @format_query_data
    def query_one_item(self, query):
        """Query for single data point"""

        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchone()


    def remove_database(self):
        """Remove the current database file using the database_name attribute."""
        os.remove(self._database_name)


    def get_var_names(self, ga):
        """Returns a list of the names of attributes of the ga."""

        # Loop through all attributes
        for var in ga.__dict__.keys():

            # Remove leading underscore
            yield (var[1:] if (var[0] == '_') else var)


    #=====================================#
    # Setters and Getters:                #
    #=====================================#


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

        # If the connection has not been set yet
        try:
            # Check if you can connect to the database
            self.create_connection()
            return self._conn

        # If the connection doesnt exist then print error
        except:
            raise Exception("""You are required to run a ga before you can connect to the database. Run ga.evolve() or ga.active()""")


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

      # If the config_id has not been set yet
      try:
          # Check if you can connect to the database
          self._config_id = self.get_current_config()
          return self._config_id

      # If the config_id doesnt exist then print error
      except:
          raise Exception("""You are required to run a ga before you can connect to the database. Run ga.evolve() or ga.active()""")


    @config_id.setter
    def config_id(self, value_input):
      """Setter function for config_id"""

      # Set the name in the ga attribute
      self._config_id = value_input
