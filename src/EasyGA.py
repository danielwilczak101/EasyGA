import random
# Import all the data structure prebuilt modules
from initialization import Population as create_population
from initialization import Chromosome as create_chromosome
from initialization import Gene as create_gene
# Structure Methods
from fitness_function import Fitness_methods
from initialization import Initialization_methods
from termination_point import Termination_methods
# Population Methods
from survivor_selection import Survivor_methods
# Manipulation Methods
from parent_selection import Parent_methods
from mutation import Mutation_methods
from crossover import Crossover_methods

class GA:
    def __init__(self):
        """Initialize the GA."""
        # Initilization variables
        self.chromosome_length = 3
        self.population_size = 5
        self.chromosome_impl = None
        self.gene_impl = None
        self.population = None
        # Termination varibles
        self.current_generation = 0
        self.generation_goal = 3

        self.current_fitness = 0
        self.fitness_goal = 3
        # Mutation variables
        self.mutation_rate = 0.03

        # Rerun already computed fitness
        self.update_fitness = False

        # Defualt EastGA implimentation structure
        self.initialization_impl = Initialization_methods.random_initialization
        self.fitness_funciton_impl = Fitness_methods.is_it_5
        # Selects which chromosomes should be automaticly moved to the next population
        #self.survivor_selection_impl = Survivor_methods.
        # Methods for accomplishing parent-selection -> Crossover -> Mutation
        # self.parent_selection_impl = Parent_methods.roulette_selection
        #self.crossover_impl = Crossover_methods.
        #self.mutation_impl = Mutation_methods.
        # The type of termination to impliment
        self.termination_impl = Termination_methods.generation_based

    def evolve_generation(self, number_of_generations = 1):
        """Evolves the ga the specified number of generations."""
        while(number_of_generations > 0):
            # If its the first generation then initialize the population
            if(self.current_generation == 0):
                # Initialize the population
                self.initialize_population()
            # First get the fitness of the population
            self.get_population_fitness(self.population.chromosome_list)
            # Selection - Triggers flags in the chromosome if its been selected
            # self.selection_impl(self)
            # Crossover - Takes the flagged chromosome_list and crosses there genetic
            # makup to make new offsprings.
            # self.crossover_impl(self)
            # Repopulate - Manipulates the population to some desired way
            # self.repopulate_impl(self)
            # Mutation - Manipulates the population very slightly
            # self.mutation_impl(self)
            # self.parent_selection_impl(self)
            # Counter for the local number of generations in evolve_generation
            number_of_generations -= 1
            # Add one to the current overall generation
            self.current_generation += 1

    def evolve(self):
        """Runs the ga until the termination point has been satisfied."""
        # While the termination point hasnt been reached keep running
        while(self.active()):
            self.evolve_generation()

    def active(self):
        """Returns if the ga should terminate base on the termination implimented"""
        # Send termination_impl the whole ga class
        return self.termination_impl(self)

    def initialize_population(self):
        """Initialize the population using the initialization
         implimentation that is currently set"""
        self.population = self.initialization_impl(self)

    def get_population_fitness(self,population):
        """Will get and set the fitness of each chromosome in the population.
        If update_fitness is set then all fitness values are updated.
        Otherwise only fitness values set to None (i.e. uninitialized
        fitness values) are updated."""
        # Get each chromosome in the population
        for chromosome in population:
            # If the fitness is not set then get its fitness or if allways getting
            # fitness is turn on then always get the fitness of the chromosome.
            if(chromosome.fitness == None or self.update_fitness == True):
                # Set the chromosomes fitness using the fitness function
                chromosome.fitness = self.fitness_funciton_impl(chromosome)

    def make_gene(self,value):
        """Let's the user create a gene."""
        return create_gene(value)

    def make_chromosome(self):
        """Let's the user create a chromosome."""
        return create_chromosome()

    def make_population(self):
        """Let's the user create a population."""
        return create_population()
