# Import square root function for ga.adapt()
from math import sqrt

import random
import sqlite3
from copy import deepcopy

# Import all the data structure prebuilt modules
from structure import Population as make_population
from structure import Chromosome as make_chromosome
from structure import Gene       as make_gene

# Structure Methods
from fitness_function  import Fitness_Examples
from termination_point import Termination_Methods

# Parent/Survivor Selection Methods
from parent_selection   import Parent_Selection
from survivor_selection import Survivor_Selection

# Genetic Operator Methods
from mutation  import Mutation_Methods
from crossover import Crossover_Methods

# Database class
from database import sql_database
from sqlite3  import Error

# Graphing package
from database import matplotlib_graph
import matplotlib.pyplot as plt


def function_info(setter):
    """Decorator for setter functions involving functions so that the name and doc-string are kept."""

    def new_setter(obj, method):
        if (new_method := setter(obj, method)) is not None:
            new_method.__name__ = method.__name__
            new_method.__doc__  = method.__doc__

    return new_setter


class Attributes:
    """Default GA attributes can be found here. If any attributes have not
    been set then they will fall back onto the default attribute. All
    attributes have been catigorized to explain sections in the ga process."""

    def __init__(
            self,
            chromosome_length            = 10,
            population_size              = 10,
            chromosome_impl              = None,
            gene_impl                    = None,
            population                   = None,
            target_fitness_type          = 'max',
            update_fitness               = False,
            parent_ratio                 = 0.10,
            selection_probability        = 0.50,
            tournament_size_ratio        = 0.10,
            current_generation           = 0,
            current_fitness              = 0,
            generation_goal              = 100,
            fitness_goal                 = None,
            tolerance_goal               = None,
            percent_converged            = 0.50,
            chromosome_mutation_rate     = 0.15,
            gene_mutation_rate           = 0.05,
            adapt_rate                   = 0.05,
            adapt_probability_rate       = 0.05,
            adapt_population_flag        = True,
            max_selection_probability    = 0.75,
            min_selection_probability    = 0.25,
            max_chromosome_mutation_rate = None,
            min_chromosome_mutation_rate = None,
            max_gene_mutation_rate       = 0.15,
            min_gene_mutation_rate       = 0.01,
            dist                         = None,
            fitness_function_impl        = None,
            make_population              = make_population,
            make_chromosome              = make_chromosome,
            make_gene                    = make_gene,
            parent_selection_impl        = None,
            crossover_individual_impl    = None,
            crossover_population_impl    = None,
            survivor_selection_impl      = None,
            mutation_individual_impl     = None,
            mutation_population_impl     = None,
            termination_impl             = None,
            Database                     = sql_database.SQL_Database,
            database_name                = 'database.db',
            sql_create_data_structure    = """CREATE TABLE IF NOT EXISTS data (
                                                  id INTEGER PRIMARY KEY,
                                                  config_id INTEGER DEFAULT NULL,
                                                  generation INTEGER NOT NULL,
                                                  fitness REAL,
                                                  chromosome TEXT
                                              ); """,
            Graph                        = matplotlib_graph.Matplotlib_Graph
        ):

        # Initilization variables
        self.chromosome_length   = chromosome_length
        self.population_size     = population_size
        self.chromosome_impl     = chromosome_impl
        self.gene_impl           = gene_impl
        self.population          = population
        self.target_fitness_type = target_fitness_type
        self.update_fitness      = update_fitness

        # Selection variables
        self.parent_ratio          = parent_ratio
        self.selection_probability = selection_probability
        self.tournament_size_ratio = tournament_size_ratio

        # Termination variables
        self.current_generation = current_generation
        self.current_fitness    = current_fitness
        self.generation_goal    = generation_goal
        self.fitness_goal       = fitness_goal
        self.tolerance_goal     = tolerance_goal
        self.percent_converged  = percent_converged

        # Mutation variables
        self.chromosome_mutation_rate = chromosome_mutation_rate
        self.gene_mutation_rate       = gene_mutation_rate

        # Adapt variables
        self.adapt_rate             = adapt_rate
        self.adapt_probability_rate = adapt_probability_rate
        self.adapt_population_flag  = adapt_population_flag

        # Bounds on probabilities when adapting
        self.max_selection_probability    = max_selection_probability
        self.min_selection_probability    = min_selection_probability
        self.max_chromosome_mutation_rate = max_chromosome_mutation_rate
        self.min_chromosome_mutation_rate = min_chromosome_mutation_rate
        self.max_gene_mutation_rate       = max_gene_mutation_rate
        self.min_gene_mutation_rate       = min_gene_mutation_rate

        # Distance between two chromosomes
        self.dist = dist

        # Default EasyGA implimentation structure
        self.fitness_function_impl = fitness_function_impl
        self.make_population       = make_population
        self.make_chromosome       = make_chromosome
        self.make_gene             = make_gene

        # Methods for accomplishing Parent-Selection -> Crossover -> Survivor_Selection -> Mutation
        self.parent_selection_impl     = parent_selection_impl
        self.crossover_individual_impl = crossover_individual_impl
        self.crossover_population_impl = crossover_population_impl
        self.survivor_selection_impl   = survivor_selection_impl
        self.mutation_individual_impl  = mutation_individual_impl
        self.mutation_population_impl  = mutation_population_impl

        # The type of termination to impliment
        self.termination_impl = termination_impl

        # Database varibles
        self.database = Database()
        self.database_name = database_name
        self.sql_create_data_structure = sql_create_data_structure

        # Graphing variables
        self.graph = Graph(self.database)


    def save_population(self):
        """Saves the current population to the database."""
        self.database.insert_current_population(self)


    def save_chromosome(self, chromosome):
        """Saves the given chromosome to the database."""
        self.database.insert_current_chromosome(self.current_generation, chromosome)


    def numeric_chromosomes(self):
        """Sets default numerical based methods"""

        # Adapt every 10th generation
        self.adapt_rate = 0.10

        # Use averaging for crossover
        self.crossover_individual_impl = Crossover_Methods.Individual.Arithmetic.average

        # Use averaging for mutation
        self.mutation_individual_impl = Mutation_Methods.Individual.Arithmetic.average

        # Euclidean norm
        self.dist = lambda chromosome_1, chromosome_2:\
            sqrt(sum(
                (gene_1.value - gene_2.value) ** 2
                for gene_1, gene_2
                in zip(chromosome_1, chromosome_2)
            ))


    def permutation_chromosomes(self, cycle = True):
        """Sets default permutation based methods"""

        cycle = int(cycle)

        self.crossover_individual_impl = Crossover_Methods.Individual.Permutation.ox1
        self.mutation_individual_impl  = Mutation_Methods.Individual.Permutation.swap_genes

        # Count the number of gene pairs they don't have in common
        def dist(chromosome_1, chromosome_2):

            # Used to set values during comprehension
            set_value = lambda arg: True

            # Index of gene from chromosome 1 in chromosome 2
            j = 0

            return sum(
                # Add 1 if they are different
                int(chromosome_1[i-1] != chromosome_2[j-1])

                # Loop over chromosome 1
                for i
                in range(1-cycle, len(chromosome_1))

                # Find index of gene from chromosome 1 in chromosome 2
                if set_value(j := chromosome_2.index_of(chromosome_1[i]))

                # Additional case to check
                if j + cycle > 0
            )

        self.dist = dist


    # Getter and setters for all required varibles


    @property
    def dist(self):
        """Getter for distance lambda which passes a reference of self in."""
        return self._dist


    @dist.setter
    @function_info
    def dist(self, method):
        """Setter for distance lambda."""
        if method is not None:
            self._dist = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._dist


    def _dist(self, chromosome_1, chromosome_2):
        """Default distance lambda. Returns the square root of the difference in fitnesses."""
        return sqrt(abs(chromosome_1.fitness - chromosome_2.fitness))


    @property
    def chromosome_impl(self):
        """Getter for chromosome implementation lambda which passes a reference of self in."""
        return self._chromosome_impl


    @chromosome_impl.setter
    @function_info
    def chromosome_impl(self, method):
        """Setter for chromosome implementation lambda."""
        if method is not None:
            self._chromosome_impl = lambda *args, **kwargs: method(*args, **kwargs)
            return self._chromosome_impl


    @property
    def gene_impl(self):
        """Getter for gene implementation lambda which passes a reference of self in."""
        return self._gene_impl


    @gene_impl.setter
    @function_info
    def gene_impl(self, method):
        """Setter for gene implementation lambda."""
        if method is not None:
            self._gene_impl = lambda *args, **kwargs: method(*args, **kwargs)
            return self._gene_impl


    def _gene_impl(self, *args, **kwargs):
        """Default gene implementation. Returns a random integer from 1 to 10."""
        return random.randint(1, 10)


    @property
    def fitness_function_impl(self):
        """Getter for fitness function lambda which passes a reference of self in."""
        return self._fitness_function_impl


    @fitness_function_impl.setter
    @function_info
    def fitness_function_impl(self, method):
        """Setter for fitness function lambda."""
        if method is not None:
            self._fitness_function_impl = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._fitness_function_impl


    def _fitness_function_impl(self, *args, **kwargs):
        """Default fitness function. Returns the number of genes that are 5."""
        return Fitness_Examples.is_it_5(*args, **kwargs)


    @property
    def parent_selection_impl(self):
        """Getter for parent selection lambda which passes a reference of self in."""

        return self._parent_selection_impl


    @parent_selection_impl.setter
    @function_info
    def parent_selection_impl(self, method):
        """Setter for parent selection lambda."""
        if method is not None:
            self._parent_selection_impl = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._parent_selection_impl


    def _parent_selection_impl(self, *args, **kwargs):
        """Default parent selection method using tournament selection."""
        return Parent_Selection.Rank.tournament(self, *args, **kwargs)


    @property
    def crossover_individual_impl(self):
        """Getter for individual crossover lambda which passes a reference of self in."""

        return self._crossover_individual_impl


    @crossover_individual_impl.setter
    @function_info
    def crossover_individual_impl(self, method):
        """Setter for individual crossover lambda."""
        if method is not None:
            self._crossover_individual_impl = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._crossover_individual_impl


    def _crossover_individual_impl(self, *args, **kwargs):
        """Default individual crossover method using single point crossover."""
        return Crossover_Methods.Individual.single_point(self, *args, **kwargs)


    @property
    def crossover_population_impl(self):
        """Getter for population crossover lambda which passes a reference of self in."""
        return self._crossover_population_impl


    @crossover_population_impl.setter
    @function_info
    def crossover_population_impl(self, method):
        """Setter for population crossover lambda."""
        if method is not None:
            self._crossover_population_impl = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._crossover_population_impl


    def _crossover_population_impl(self, *args, **kwargs):
        """Default population crossover method using sequential selection."""
        return Crossover_Methods.Population.sequential_selection(self, *args, **kwargs)


    @property
    def survivor_selection_impl(self):
        """Getter for survivor selection lambda which passes a reference of self in."""
        return self._survivor_selection_impl


    @survivor_selection_impl.setter
    @function_info
    def survivor_selection_impl(self, method):
        """Setter for survivor selection lambda."""
        if method is not None:
            self._survivor_selection_impl = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._survivor_selection_impl


    def _survivor_selection_impl(self, *args, **kwargs):
        """Default survivor selection method using the fill in best method."""
        return Survivor_Selection.fill_in_best(self, *args, **kwargs)


    @property
    def mutation_individual_impl(self):
        """Getter for individual mutation lambda which passes a reference of self in."""
        return self._mutation_individual_impl


    @mutation_individual_impl.setter
    @function_info
    def mutation_individual_impl(self, method):
        """Setter for individual mutation lambda."""
        if method is not None:
            self._mutation_individual_impl = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._mutation_individual_impl


    def _mutation_individual_impl(self, *args, **kwargs):
        """Default individual mutation method by randomizing individual genes."""
        return Mutation_Methods.Individual.individual_genes(self, *args, **kwargs)


    @property
    def mutation_population_impl(self):
        """Getter for population mutation lambda which passes a reference of self in."""
        return self._mutation_population_impl


    @mutation_population_impl.setter
    @function_info
    def mutation_population_impl(self, method):
        """Setter for population mutation lambda."""
        if method is not None:
            self._mutation_population_impl = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._mutation_population_impl


    def _mutation_population_impl(self, *args, **kwargs):
        """Default population mutation method selects chromosomes randomly while avoiding the best."""
        return Mutation_Methods.Population.random_avoid_best(self, *args, **kwargs)


    @property
    def termination_impl(self):
        """Getter for termination lambda which passes a reference of self in."""
        return self._termination_impl


    @termination_impl.setter
    @function_info
    def termination_impl(self, method):
        """Setter for termination lambda."""
        if method is not None:
            self._termination_impl = lambda *args, **kwargs: method(self, *args, **kwargs)
            return self._termination_impl


    def _termination_impl(self, *args, **kwargs):
        """Default termination method by testing the fitness, generation, and tolerance goals."""
        return Termination_Methods.fitness_generation_tolerance(self, *args, **kwargs)


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
        """Setter function for target fitness type."""

        self._target_fitness_type = value_input


    @property
    def max_chromosome_mutation_rate(self):
        """Getter function for max chromosome mutation rate"""

        return self._max_chromosome_mutation_rate


    @max_chromosome_mutation_rate.setter
    def max_chromosome_mutation_rate(self, value_input):
        """Setter function with error checking and default value for max chromosome mutation rate"""

        # Default value
        if value_input is None:
            self._max_chromosome_mutation_rate = min(self.chromosome_mutation_rate*2, (1+self.chromosome_mutation_rate)/2)

        # Otherwise check value
        elif 0 <= value_input <= 1:
            self._max_chromosome_mutation_rate = value_input

        # Throw error
        else:
            raise ValueError("Max chromosome mutation rate must be between 0 and 1")


    @property
    def min_chromosome_mutation_rate(self):
        """Getter function for min chromosome mutation rate"""

        return self._min_chromosome_mutation_rate


    @min_chromosome_mutation_rate.setter
    def min_chromosome_mutation_rate(self, value_input):
        """Setter function with error checking and default value for min chromosome mutation rate"""

        # Default value
        if value_input is None:
            self._min_chromosome_mutation_rate = self.chromosome_mutation_rate/2

        # Otherwise check value
        elif 0 <= value_input <= 1:
            self._min_chromosome_mutation_rate = value_input

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
