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
    """SAMPLE TEXT"""

    def __init__(self,
            chromosome_length,
            population_size,
            chromosome_impl,
            gene_impl,
            population,
            target_fitness_type,
            update_fitness,
            parent_ratio,
            selection_probability,
            tournament_size_ratio,
            current_generation,
            current_fitness,
            generation_goal,
            fitness_goal,
            chromosome_mutation_rate,
            gene_mutation_rate,
            initialization_impl,
            fitness_function_impl,
            make_population,
            make_chromosome,
            make_gene,
            parent_selection_impl,
            crossover_individual_impl,
            crossover_population_impl,
            survivor_selection_impl,
            mutation_individual_impl,
            mutation_population_impl,
            termination_impl
            ):
        """Initialize the GA."""

        # Initilization variables
        self.chromosome_length   = 10    if chromosome_length   is None else chromosome_length
        self.population_size     = 10    if population_size     is None else population_size
        self.chromosome_impl     = chromosome_impl
        self.gene_impl           = gene_impl
        self.population          = population
        self.target_fitness_type = 'max' if target_fitness_type is None else target_fitness_type
        self.update_fitness      = True  if update_fitness      is None else update_fitness

        # Selection variables
        self.parent_ratio = 0.10          if parent_ratio          is None else parent_ratio
        self.selection_probability = 0.75 if selection_probability is None else selection_probability
        self.tournament_size_ratio = 0.10 if tournament_size_ratio is None else tournament_size_ratio

        # Termination variables
        self.current_generation = 0  if current_generation is None else current_generation
        self.current_fitness    = 0  if current_fitness    is None else current_fitness
        self.generation_goal    = 15 if generation_goal    is None else generation_goal
        self.fitness_goal       = fitness_goal

        # Mutation variables
        self.chromosome_mutation_rate = 0.15 if chromosome_mutation_rate is None else chromosome_mutation_rate
        self.gene_mutation_rate       = 0.03 if gene_mutation_rate       is None else gene_mutation_rate

        # Default EasyGA implimentation structure
        self.initialization_impl   = Initialization_Methods.random_initialization if initialization_impl is None else initialization_impl
        self.fitness_function_impl = Fitness_Examples.is_it_5 if fitness_function_impl is None else fitness_function_impl
        self.make_population       = create_population if create_population is None else create_population
        self.make_chromosome       = create_chromosome if create_chromosome is None else create_chromosome
        self.make_gene             = create_gene       if create_gene       is None else create_gene

        # Methods for accomplishing Parent-Selection -> Crossover -> Survivor_Selection -> Mutation
        self.parent_selection_impl     = Parent_Selection.Rank.tournament if parent_selection_impl is None else parent_selection_impl
        self.crossover_individual_impl = Crossover_Methods.Individual.single_point if crossover_individual_impl is None else crossover_individual_impl
        self.crossover_population_impl = Crossover_Methods.Population.sequential_selection if crossover_population_impl is None else crossover_population_impl
        self.survivor_selection_impl   = Survivor_Selection.fill_in_best if survivor_selection_impl is None else survivor_selection_impl
        self.mutation_individual_impl  = Mutation_Methods.Individual.single_gene if mutation_individual_impl is None else mutation_individual_impl
        self.mutation_population_impl  = Mutation_Methods.Population.random_selection if mutation_population_impl is None else mutation_population_impl

        # The type of termination to impliment
        self.termination_impl = Termination_Methods.fitness_and_generation_based if termination_impl is None else termination_impl


    # Getter and setters for all varibles
    @property
    def chromosome_length(self):
        """SAMPLE TEXT"""
        return self._chromosome_length

    @chromosome_length.setter
    def chromosome_length(self, value_input):
        if(not isinstance(value_input, int) or value_input <= 0):
            raise ValueError("Chromosome length must be integer greater then 0")
        self._chromosome_length = value_input


    @property
    def population_size(self):
        return self._population_size

    @population_size.setter
    def population_size(self, value_input):
        if(not isinstance(value_input, int) or value_input <= 0):
            raise ValueError("Population length must be integer greater then 0")
        self._population_size = value_input
