import random

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

class attributes:
    """Default GA attributes can be found here. If any attributes have not
    been set then they will fall back onto the default attribute. All
    attributes have been catigorized to explain sections in the ga process."""

    def __init__(self):

        # Initilization variables
        self.chromosome_length   = 10
        self.population_size     = 10
        self.chromosome_impl     = None
        self.gene_impl           = lambda: random.randint(1, 10)
        self.population          = None
        self.target_fitness_type = 'max'
        self.update_fitness      = True

        # Selection variables
        self.parent_ratio          = 0.1
        self.selection_probability = 0.75
        self.tournament_size_ratio = 0.1

        # Termination variables
        self.current_generation = 0
        self.current_fitness    = 0
        self.generation_goal    = 15
        self.fitness_goal       = None

        # Mutation variables
        self.gene_mutation_rate       = 0.03
        self.chromosome_mutation_rate = 0.15

        # Default EasyGA implimentation structure
        self.initialization_impl   = Initialization_Methods.random_initialization
        self.fitness_function_impl = Fitness_Examples.is_it_5
        self.make_population       = create_population
        self.make_chromosome       = create_chromosome
        self.make_gene             = create_gene

        # Methods for accomplishing Parent-Selection -> Crossover -> Survivor_Selection -> Mutation
        self.parent_selection_impl     = Parent_Selection.Rank.tournament
        self.crossover_individual_impl = Crossover_Methods.Individual.single_point
        self.crossover_population_impl = Crossover_Methods.Population.sequential_selection
        self.survivor_selection_impl   = Survivor_Selection.fill_in_best
        self.mutation_individual_impl  = Mutation_Methods.Individual.single_gene
        self.mutation_population_impl  = Mutation_Methods.Population.random_selection

        # The type of termination to impliment
        self.termination_impl = Termination_Methods.fitness_and_generation_based

        # Database varibles
        self.database_name = "database.db"

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
