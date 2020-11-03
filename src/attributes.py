import random
import sqlite3

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
from database import database
from sqlite3 import Error

class Attributes:
    """Default GA attributes can be found here. If any attributes have not
    been set then they will fall back onto the default attribute. All
    attributes have been catigorized to explain sections in the ga process."""

    def __init__(self, attributes):

        # Default settings for the GA
        default_attributes = {
            'chromosome_length'         : 10,
            'population_size'           : 10,
            'chromosome_impl'           : None,
            'gene_impl'                 : lambda: random.randint(1, 10),
            'population'                : None,
            'target_fitness_type'       : 'max',
            'update_fitness'            : True,
            'parent_ratio'              : 0.10,
            'selection_probability'     : 0.50,
            'tournament_size_ratio'     : 0.10,
            'current_generation'        : 0,
            'current_fitness'           : 0,
            'generation_goal'           : 15,
            'fitness_goal'              : None,
            'chromosome_mutation_rate'  : 0.15,
            'gene_mutation_rate'        : 0.03,
            'initialization_impl'       : Initialization_Methods.random_initialization,
            'fitness_function_impl'     : Fitness_Examples.is_it_5,
            'make_population'           : create_population,
            'make_chromosome'           : create_chromosome,
            'make_gene'                 : create_gene,
            'parent_selection_impl'     : Parent_Selection.Rank.tournament,
            'crossover_individual_impl' : Crossover_Methods.Individual.single_point,
            'crossover_population_impl' : Crossover_Methods.Population.sequential_selection,
            'survivor_selection_impl'   : Survivor_Selection.fill_in_best,
            'mutation_individual_impl'  : Mutation_Methods.Individual.single_gene,
            'mutation_population_impl'  : Mutation_Methods.Population.random_selection,
            'termination_impl'          : Termination_Methods.fitness_and_generation_based,
            'database'                  : None,
            'database_name'             : r"database.db",
            'sql_create_data_structure' : """ CREATE TABLE IF NOT EXISTS data (
                                                id integer PRIMARY KEY,
                                                generation integer NOT NULL,
                                                fitness DOUBLE,
                                                chromosome text
                                            ); """

        }

        # Filling in the default settings
        for attribute in default_attributes.keys():
            if attribute not in attributes.keys():
                attributes[attribute] = default_attributes[attribute]

        # Initilization variables
        self.chromosome_length   = attributes['chromosome_length']
        self.population_size     = attributes['population_size']
        self.chromosome_impl     = attributes['chromosome_impl']
        self.gene_impl           = attributes['gene_impl']
        self.population          = attributes['population']
        self.target_fitness_type = attributes['target_fitness_type']
        self.update_fitness      = attributes['update_fitness']

        # Selection variables
        self.parent_ratio          = attributes['parent_ratio']
        self.selection_probability = attributes['selection_probability']
        self.tournament_size_ratio = attributes['tournament_size_ratio']

        # Termination variables
        self.current_generation = attributes['current_generation']
        self.current_fitness    = attributes['current_fitness']
        self.generation_goal    = attributes['generation_goal']
        self.fitness_goal       = attributes['fitness_goal']

        # Mutation variables
        self.chromosome_mutation_rate = attributes['chromosome_mutation_rate']
        self.gene_mutation_rate       = attributes['gene_mutation_rate']

        # Default EasyGA implimentation structure
        self.initialization_impl   = attributes['initialization_impl']
        self.fitness_function_impl = attributes['fitness_function_impl']
        self.make_population       = attributes['make_population']
        self.make_chromosome       = attributes['make_chromosome']
        self.make_gene             = attributes['make_gene']

        # Methods for accomplishing Parent-Selection -> Crossover -> Survivor_Selection -> Mutation
        self.parent_selection_impl     = attributes['parent_selection_impl']
        self.crossover_individual_impl = attributes['crossover_individual_impl']
        self.crossover_population_impl = attributes['crossover_population_impl']
        self.survivor_selection_impl   = attributes['survivor_selection_impl']
        self.mutation_individual_impl  = attributes['mutation_individual_impl']
        self.mutation_population_impl  = attributes['mutation_population_impl']

        # The type of termination to impliment
        self.termination_impl = attributes['termination_impl']

        # Database varibles
        self.database_name = attributes['database_name']

        # Database varibles
        self.database = attributes['database']
        self.database_name = attributes['database_name']
        self.sql_create_data_structure = attributes['sql_create_data_structure']


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
