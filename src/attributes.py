import random
import sqlite3
from copy import deepcopy

# Import all the data structure prebuilt modules
from structure import Population as create_population
from structure import Chromosome as create_chromosome
from structure import Gene as create_gene

# Structure Methods
from fitness_function  import Fitness_Examples
from initialization    import Initialization_Methods
from termination_point import Termination_Methods

# Parent/Survivor Selection Methods
from parent_selection   import Parent_Selection
from survivor_selection import Survivor_Selection

# Genetic Operator Methods
from mutation  import Mutation_Methods
from crossover import Crossover_Methods

# Database class
from database import sql_database
from sqlite3 import Error

# Graphing package
from database import matplotlib_graph
import matplotlib.pyplot as plt


class Attributes:
    """Default GA attributes can be found here. If any attributes have not
    been set then they will fall back onto the default attribute. All
    attributes have been catigorized to explain sections in the ga process."""

    target_fitness_type_dict = {
            'min'          : 'min',
            'minimize'     : 'min',
            'minimise'     : 'min',
            'minimization' : 'min',
            'minimisation' : 'min',
            'max'          : 'max',
            'maximize'     : 'max',
            'maximise'     : 'max',
            'maximization' : 'max',
            'maximisation' : 'max'
        }

    def __init__(self,
            chromosome_length           = 10,
            population_size             = 10,
            chromosome_impl             = None,
            gene_impl                   = lambda: random.randint(1, 10),
            population                  = None,
            target_fitness_type         = 'max',
            update_fitness              = True,
            parent_ratio                = 0.10,
            selection_probability       = 0.50,
            tournament_size_ratio       = 0.10,
            current_generation          = 0,
            current_fitness             = 0,
            generation_goal             = 15,
            fitness_goal                = None,
            tolerance_goal              = None,
            percent_converged           = 0.50,
            chromosome_mutation_rate    = 0.15,
            gene_mutation_rate          = 0.05,
            initialization_impl         = Initialization_Methods.random_initialization,
            fitness_function_impl       = Fitness_Examples.is_it_5,
            make_population             = create_population,
            make_chromosome             = create_chromosome,
            make_gene                   = create_gene,
            parent_selection_impl       = Parent_Selection.Rank.tournament,
            crossover_individual_impl   = Crossover_Methods.Individual.single_point,
            crossover_population_impl   = Crossover_Methods.Population.sequential_selection,
            survivor_selection_impl     = Survivor_Selection.fill_in_best,
            mutation_individual_impl    = Mutation_Methods.Individual.individual_genes,
            mutation_population_impl    = Mutation_Methods.Population.random_selection_then_cross,
            termination_impl            = Termination_Methods.fitness_generation_tolerance,
            Database                    = sql_database.SQL_Database,
            database_name               = 'database.db',
            sql_create_data_structure   = """CREATE TABLE IF NOT EXISTS data (
                                                id INTEGER PRIMARY KEY,
                                                config_id INTEGER DEFAULT NULL,
                                                generation INTEGER NOT NULL,
                                                fitness REAL,
                                                chromosome TEXT
                                            ); """,
            Graph                       = matplotlib_graph.Matplotlib_Graph
        ):

        # Initilization variables
        self.chromosome_length   = deepcopy(chromosome_length)
        self.population_size     = deepcopy(population_size)
        self.chromosome_impl     = deepcopy(chromosome_impl)
        self.gene_impl           = deepcopy(gene_impl)
        self.population          = deepcopy(population)
        self.target_fitness_type = deepcopy(target_fitness_type)
        self.update_fitness      = deepcopy(update_fitness)

        # Selection variables
        self.parent_ratio          = deepcopy(parent_ratio)
        self.selection_probability = deepcopy(selection_probability)
        self.tournament_size_ratio = deepcopy(tournament_size_ratio)

        # Termination variables
        self.current_generation = deepcopy(current_generation)
        self.current_fitness    = deepcopy(current_fitness)
        self.generation_goal    = deepcopy(generation_goal)
        self.fitness_goal       = deepcopy(fitness_goal)
        self.tolerance_goal     = deepcopy(tolerance_goal)
        self.percent_converged  = deepcopy(percent_converged)

        # Mutation variables
        self.chromosome_mutation_rate = deepcopy(chromosome_mutation_rate)
        self.gene_mutation_rate       = deepcopy(gene_mutation_rate)

        # Default EasyGA implimentation structure
        self.initialization_impl   = deepcopy(initialization_impl)
        self.fitness_function_impl = deepcopy(fitness_function_impl)
        self.make_population       = deepcopy(make_population)
        self.make_chromosome       = deepcopy(make_chromosome)
        self.make_gene             = deepcopy(make_gene)

        # Methods for accomplishing Parent-Selection -> Crossover -> Survivor_Selection -> Mutation
        self.parent_selection_impl     = deepcopy(parent_selection_impl)
        self.crossover_individual_impl = deepcopy(crossover_individual_impl)
        self.crossover_population_impl = deepcopy(crossover_population_impl)
        self.survivor_selection_impl   = deepcopy(survivor_selection_impl)
        self.mutation_individual_impl  = deepcopy(mutation_individual_impl)
        self.mutation_population_impl  = deepcopy(mutation_population_impl)

        # The type of termination to impliment
        self.termination_impl = deepcopy(termination_impl)

        # Database varibles
        self.database = Database()
        self.database_name = deepcopy(database_name)
        self.sql_create_data_structure = deepcopy(sql_create_data_structure)

        # Graphing variables
        self.graph = Graph(self.database)


    def save_population(self):
        """Saves the current population to the database."""
        self.database.insert_current_population(self)


    def save_chromosome(self, chromosome):
        """Saves the given chromosome to the database."""
        self.database.insert_current_chromosome(self.current_generation, chromosome)


    # Getter and setters for all required varibles
    @property
    def chromosome_length(self):
        """Getter function for chromosome length"""

        return self._chromosome_length


    @chromosome_length.setter
    def chromosome_length(self, value_input):
        """Setter function with error checking for chromosome length"""

        # If the chromosome length is less then or equal 0 throw error
        if(not isinstance(value_input, int) or value_input <= 0):
            raise ValueError("Chromosome length must be integer greater then 0")
        self._chromosome_length = value_input


    @property
    def population_size(self):
        """Getter function for population size"""

        return self._population_size


    @population_size.setter
    def population_size(self, value_input):
        """Setter function with error checking for population size"""

        # If the population size is less then or equal 0 throw error
        if(not isinstance(value_input, int) or value_input <= 0):
            raise ValueError("Population length must be integer greater then 0")
        self._population_size = value_input


    @property
    def target_fitness_type(self):
        """Getter function for target fitness type."""

        return self._target_fitness_type


    @target_fitness_type.setter
    def target_fitness_type(self, value_input):
        """Setter function for target fitness type for
        converting input to min/max."""

        if value_input in self.target_fitness_type_dict.keys():
            self._target_fitness_type = self.target_fitness_type_dict[value_input]
        else:
            self._target_fitness_type = value_input
