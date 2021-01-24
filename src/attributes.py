# Import signature tool to check if functions start with self or ga
from inspect import signature

# Import math for square root (ga.dist()) and ceil (crossover methods)
import math

import random
import sqlite3
from copy import deepcopy

# Import all the data structure prebuilt modules
from structure import Population as make_population
from structure import Chromosome as make_chromosome
from structure import Gene       as make_gene

# Misc. Methods
from fitness_examples import Fitness_Examples
from termination import Termination

# Parent/Survivor Selection Methods
from parent   import Parent
from survivor import Survivor

# Genetic Operator Methods
from crossover import Crossover
from mutation  import Mutation

# Database class
from database import sql_database
from sqlite3  import Error

# Graphing package
from database import matplotlib_graph
import matplotlib.pyplot as plt


class Attributes:
    """Default GA attributes can be found here. If any attributes have not
    been set then they will fall back onto the default attribute. All
    attributes have been catigorized to explain sections in the ga process."""

    #=====================#
    # Default GA methods: #
    #=====================#

    # Default EasyGA implimentation structure
    fitness_function_impl = Fitness_Examples.is_it_5
    make_population = make_population
    make_chromosome = make_chromosome
    make_gene = make_gene

    # Methods for accomplishing Parent-Selection -> Crossover -> Survivor_Selection -> Mutation -> Termination
    parent_selection_impl = Parent.Rank.tournament
    crossover_individual_impl = Crossover.Individual.single_point
    crossover_population_impl = Crossover.Population.sequential
    survivor_selection_impl = Survivor.fill_in_best
    mutation_individual_impl = Mutation.Individual.individual_genes
    mutation_population_impl = Mutation.Population.random_avoid_best
    termination_impl = Termination.fitness_generation_tolerance


    def dist(self, chromosome_1, chromosome_2):
        """Default distance lambda. Returns the square root of the difference in fitnesses."""
        return math.sqrt(abs(chromosome_1.fitness - chromosome_2.fitness))


    def weighted_random(self, weight):
        """Returns a random value between 0 and 1. Returns values between the weight and the
        nearest of 0 and 1 less frequently than between weight and the farthest of 0 and 1."""

        rand_num = random.random()
        if rand_num < weight:
            return (1-weight) * rand_num / weight
        else:
            return 1 - weight * (1-rand_num) / (1-weight)


    def gene_impl(self, *args, **kwargs):
        """Default gene implementation. Returns a random integer from 1 to 10."""
        return random.randint(1, 10)


    chromosome_impl = None


    #=====================================#
    # Special built-in class __methods__: #
    #=====================================#

    def __init__(
            self,
            *,
            # Attributes must be passed in using kwargs

            run  = 0,

            chromosome_length = 10,
            population_size = 10,
            population = None,
            target_fitness_type = 'max',
            update_fitness = False,

            parent_ratio = 0.10,
            selection_probability = 0.50,
            tournament_size_ratio = 0.10,

            current_generation = 0,
            current_fitness = 0,

            generation_goal   = 100,
            fitness_goal      = None,
            tolerance_goal    = None,
            percent_converged = 0.50,

            chromosome_mutation_rate = 0.15,
            gene_mutation_rate = 0.05,

            adapt_rate = 0.05,
            adapt_probability_rate = 0.05,
            adapt_population_flag  = True,

            max_selection_probability = 0.75,
            min_selection_probability = 0.25,
            max_chromosome_mutation_rate = None,
            min_chromosome_mutation_rate = None,
            max_gene_mutation_rate = 0.15,
            min_gene_mutation_rate = 0.01,

            Database = sql_database.SQL_Database,
            database_name = 'database.db',
            sql_create_data_structure = f"""
            CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY,
            config_id INTEGER DEFAULT NULL,
            generation INTEGER NOT NULL,
            fitness REAL,
            chromosome TEXT
            ); """,

            Graph = matplotlib_graph.Matplotlib_Graph,

            **kwargs
        ):

        # Keep track of the current run
        self.run = run

        # Initilization variables
        self.chromosome_length = chromosome_length
        self.population_size = population_size
        self.population = population
        self.target_fitness_type = target_fitness_type
        self.update_fitness = update_fitness

        # Selection variables
        self.parent_ratio = parent_ratio
        self.selection_probability = selection_probability
        self.tournament_size_ratio = tournament_size_ratio

        # Termination variables
        self.current_generation = current_generation
        self.current_fitness = current_fitness
        self.generation_goal = generation_goal
        self.fitness_goal = fitness_goal
        self.tolerance_goal = tolerance_goal
        self.percent_converged = percent_converged

        # Mutation variables
        self.chromosome_mutation_rate = chromosome_mutation_rate
        self.gene_mutation_rate = gene_mutation_rate

        # Adapt variables
        self.adapt_rate = adapt_rate
        self.adapt_probability_rate = adapt_probability_rate
        self.adapt_population_flag  = adapt_population_flag

        # Bounds on probabilities when adapting
        self.max_selection_probability = max_selection_probability
        self.min_selection_probability = min_selection_probability
        self.max_chromosome_mutation_rate = max_chromosome_mutation_rate
        self.min_chromosome_mutation_rate = min_chromosome_mutation_rate
        self.max_gene_mutation_rate = max_gene_mutation_rate
        self.min_gene_mutation_rate = min_gene_mutation_rate

        # Database varibles
        self.database = Database()
        self.database_name = database_name
        self.sql_create_data_structure = sql_create_data_structure

        # Graphing variables
        self.graph = Graph(self.database)

        # Any other custom kwargs?
        for name, value in kwargs.items():
            self.__setattr__(name, value)


    def __setattr__(self, name, value):
        """Custom setter for using

            self.name = value

        which follows the following guidelines:
        - if self.name is a property, the specific property setter is used
        - else if value is callable and the first parameter is either 'self' or 'ga', self is passed in as the first parameter
        - else if value is not None or self.name is not set, assign it like normal
        """

        # Check for property
        if hasattr(type(self), name) and isinstance(getattr(type(self), name), property):
            getattr(type(self), name).fset(self, value)

        # Check for function
        elif callable(value) and next(iter(signature(value).parameters), None) in ('self', 'ga'):
            foo = lambda *args, **kwargs: value(self, *args, **kwargs)
            # Reassign name and doc-string for documentation
            foo.__name__ = value.__name__
            foo.__doc__  = value.__doc__
            self.__dict__[name] = foo

        # Assign like normal unless None or undefined self.name
        elif value is not None or not hasattr(self, name):
            self.__dict__[name] = value


    #============================#
    # Built-in database methods: #
    #============================#


    def save_population(self):
        """Saves the current population to the database."""
        self.database.insert_current_population(self)


    def save_chromosome(self, chromosome):
        """Saves the given chromosome to the database."""
        self.database.insert_current_chromosome(self.current_generation, chromosome)


    #===================#
    # Built-in options: #
    #===================#


    def numeric_chromosomes(self):
        """Sets default numerical based methods"""

        # Adapt every 10th generation
        self.adapt_rate = 0.10

        # Use averaging for crossover
        self.crossover_individual_impl = Crossover.Individual.Arithmetic.average

        # Use averaging for mutation
        self.mutation_individual_impl = Mutation.Individual.individual_genes

        # Euclidean norm
        self.dist = lambda self, chromosome_1, chromosome_2:\
            math.sqrt(sum(
                (gene_1.value - gene_2.value) ** 2
                for gene_1, gene_2
                in zip(chromosome_1, chromosome_2)
            ))


    def permutation_chromosomes(self, cycle = True):
        """Sets default permutation based methods"""

        cycle = int(cycle)

        self.crossover_individual_impl = Crossover.Individual.Permutation.ox1
        self.mutation_individual_impl  = Mutation.Individual.Permutation.swap_genes

        def dist(self, chromosome_1, chromosome_2):
            """Count the number of gene pairs they don't have in common."""

            return sum(
                1
                for x, y
                in zip(chromosome_1, chromosome_2)
                if x != y
            )

        self.dist = dist


    #===========================#
    # Getter/setter properties: #
    #===========================#


    @property
    def run(self):
        """Getter function for the run counter."""
        return self._run


    @run.setter
    def run(self, value):
        """Setter function for the run counter."""
        if not(isinstance(value, int) and value >= 0):
            raise ValueError("ga.run counter must be an integer greater than or equal to 0.")
        self._run = value


    @property
    def current_generation(self):
        """Getter function for the current generation."""
        return self._current_generation


    @current_generation.setter
    def current_generation(self, generation):
        """Setter function for the current generation."""

        if not isinstance(generation, int) or generation < 0:
            raise ValueError("ga.current_generation must be an integer greater than or equal to 0")

        self._current_generation = generation


    @property
    def chromosome_length(self):
        """Getter function for chromosome length"""
        return self._chromosome_length


    @chromosome_length.setter
    def chromosome_length(self, length):
        """Setter function with error checking for chromosome length"""

        if(not isinstance(length, int) or length <= 0):
            raise ValueError("Chromosome length must be integer greater than 0")

        self._chromosome_length = length


    @property
    def population_size(self):
        """Getter function for population size"""

        return self._population_size


    @population_size.setter
    def population_size(self, size):
        """Setter function with error checking for population size"""

        if(not isinstance(size, int) or size <= 0):
            raise ValueError("Population size must be integer greater than 0")

        self._population_size = size


    @property
    def target_fitness_type(self):
        """Getter function for target fitness type."""

        return self._target_fitness_type


    @target_fitness_type.setter
    def target_fitness_type(self, target_fitness_type):
        """Setter function for target fitness type."""

        self._target_fitness_type = target_fitness_type


    @property
    def max_chromosome_mutation_rate(self):
        """Getter function for max chromosome mutation rate"""

        return self._max_chromosome_mutation_rate


    @max_chromosome_mutation_rate.setter
    def max_chromosome_mutation_rate(self, rate):
        """Setter function with error checking and default value for max chromosome mutation rate"""

        # Default value
        if rate is None:
            self._max_chromosome_mutation_rate = min(self.chromosome_mutation_rate*2, (1+self.chromosome_mutation_rate)/2)

        # Otherwise check value
        elif 0 <= rate <= 1:
            self._max_chromosome_mutation_rate = rate

        # Throw error
        else:
            raise ValueError("Max chromosome mutation rate must be between 0 and 1")


    @property
    def min_chromosome_mutation_rate(self):
        """Getter function for min chromosome mutation rate"""

        return self._min_chromosome_mutation_rate


    @min_chromosome_mutation_rate.setter
    def min_chromosome_mutation_rate(self, rate):
        """Setter function with error checking and default value for min chromosome mutation rate"""

        # Default value
        if rate is None:
            self._min_chromosome_mutation_rate = self.chromosome_mutation_rate/2

        # Otherwise check value
        elif 0 <= rate <= 1:
            self._min_chromosome_mutation_rate = rate

        # Throw error
        else:
            raise ValueError("Min chromosome mutation rate must be between 0 and 1")


    @property
    def database_name(self):
        """Getter function for the database name"""

        return self._database_name


    @database_name.setter
    def database_name(self, value_input):
        """Setter function with error checking for the database name"""

        # Update the database class of the name change
        self.database._database_name = value_input

        # Set the name in the ga attribute
        self._database_name = value_input
