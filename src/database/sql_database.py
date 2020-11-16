import sqlite3
from sqlite3 import Error
import os


class SQL_Database:
    """Main database class that controls all the functionality for input /
    out of the database using SQLite3."""

    sql_types_dict = [int, float, str]

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
        """ Insert one chromosome into the database"""

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

        # Structure the insert data
        db_chromosome_list = [
                (ga.current_generation, chromosome.fitness, '[chromosome]')
                    for chromosome in ga.population.get_chromosome_list()
            ]

        # Create sql query structure
        sql = ''' INSERT INTO data(generation,fitness,chromosome)
         VALUES(?,?,?) '''

        cur = self.conn.cursor()
        cur.executemany(sql, db_chromosome_list)
        self.conn.commit()
        return cur.lastrowid


    def create_all_tables(self, ga):
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
            self.create_table(ga.sql_create_config_structure)
        else:
            print("Error! cannot create the database connection.")


    def insert_config(self,ga):
        """Insert the configuration attributes into the config."""

        # Structure the insert data
        db_config_list = [
            ga.chromosome_length,
            ga.population_size,
            chromosome_impl,
            gene_impl,
            ga.target_fitness_type,
            ga.update_fitness,
            ga.parent_ratio,
            ga.selection_probability,
            ga.tournament_size_ratio,
            ga.current_generation,
            float(ga.current_fitness),
            ga.generation_goal,
            ga.fitness_goal,
            ga.tolerance_goal,
            ga.percent_converged,
            ga.chromosome_mutation_rate,
            ga.gene_mutation_rate,
            ga.initialization_impl,
            ga.fitness_function_impl,
            ga.parent_selection_impl,
            ga.crossover_individual_impl,
            ga.crossover_population_impl,
            ga.survivor_selection_impl,
            ga.mutation_individual_impl,
            ga.mutation_population_impl,
            ga.termination_impl,
            ga.database_name
            ]

        # Clean up so the sqlite database accepts the data structure
        for i in range(len(db_config_list)):
            if callable(db_config_list[i]):
                db_config_list[i] = db_config_list[i].__name__
            elif type(db_config_list[i]) not in self.sql_types_dict:
                db_config_list[i] = str(db_config_list[i])

        # For some reason it has to be in var = array(tuple()) form
        db_config_list = [tuple(db_config_list)]

        # Create sql query structure
        sql = f'''INSERT INTO config (chromosome_length,
        population_size,
        chromosome_impl,
        gene_impl,
        target_fitness_type,
        update_fitness,
        parent_ratio,
        selection_probability,
        tournament_size_ratio,
        current_generation,
        current_fitness,
        generation_goal,
        fitness_goal,
        tolerance_goal,
        percent_converged,
        chromosome_mutation_rate,
        gene_mutation_rate,
        initialization_impl,
        fitness_function_impl,
        parent_selection_impl,
        crossover_individual_impl,
        crossover_population_impl,
        survivor_selection_impl,
        mutation_individual_impl,
        mutation_population_impl,
        termination_impl,
        database_name) VALUES({(',?'*len(db_config_list))[1:]}) '''

        # Execute sql query
        cur = self.conn.cursor()
        cur.executemany(sql, db_config_list)
        self.conn.commit()
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


    def get_generation_total_fitness(self):
        """Get each generations total fitness sum from the database """

        query_data = self.query_all("SELECT SUM(fitness) FROM data GROUP BY generation;")

        # Format the fitness data into one list
        formated_query_data = [i[0] for i in query_data]

        return formated_query_data


    def get_total_generations(self):
        """Get the total generations from the database"""

        query_data = self.query_one_item("SELECT COUNT(DISTINCT generation) FROM data;")

        return query_data


    def get_highest_chromosome(self):
        """Get the highest fitness of each generation"""

        query_data = self.query_all("select fitness, max(fitness) from data group by generation")

        # Format the fitness data into one list
        formated_query_data = [i[0] for i in query_data]

        return formated_query_data;


    def get_lowest_chromosome(self):
        """Get the lowest fitness of each generation"""

        query_data = self.query_all("select fitness, min(fitness) from data group by generation")

        # Format the fitness data into one list
        formated_query_data = [i[0] for i in query_data]

        return formated_query_data;
