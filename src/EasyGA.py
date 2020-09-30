import random

# Import all the data prebuilt modules
from initialization import population as create_population
from initialization import chromosome as create_chromosome
from initialization import gene as create_gene
# Import the default fitness function
from fitness_function import example_is_it_5
# Import default termination points
from termination_point import generation_based
from termination_point import fitness_based
# Import functionality defaults
from initialization import random_initialization

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
        self.max_generations = 3
        self.current_fitness = 0
        self.goal_fitness = 3
        # Mutation variables
        self.mutation_rate = 0.03


        # Defualt EastGA implimentation structure
        self.initialization_impl = random_initialization
        self.fitness_funciton_impl = example_is_it_5
        #self.mutation_impl = PerGeneMutation(Mutation_rate)
        #self.selection_impl = TournamentSelection()
        #self.crossover_impl = FastSinglePointCrossover()
        self.termination_impl = generation_based

        # If we want the fitnesses to be updated by the computer
        self.update_fitness = True

    def initialize_population(self):
        """Initialize the population using the initialization
         implimentation that is currently set"""
        self.population = self.initialization_impl(
        self.population_size,
        self.chromosome_length,
        self.chromosome_impl,
        self.gene_impl)

    def get_population_fitness(self,population):
        """Will get and set the fitness of each chromosome in the population"""
        # Get each chromosome in the population
        for chromosome in population:
            # Set the chromosomes fitness using the fitness function
            chromosome.fitness = self.fitness_funciton_impl(chromosome)

    def evolve(self):
        """Runs the ga until the termination point has been satisfied."""
        # While the termination point hasnt been reached keep running
        while(self.active()):
            self.evolve_generation()


    def active(self):
        """Returns if the ga should terminate base on the termination implimented"""
        # Send termination_impl the whole ga class
        return self.termination_impl(self)


    def evolve_generation(self, number_of_generations = 1):
        """Evolves the ga the specified number of generations.
        If update_fitness is set then all fitness values are updated.
        Otherwise only fitness values set to None (i.e. uninitialized
        fitness values) are updated."""
        while(number_of_generations > 0):
            # If its the first generation then initialize the population
            if(self.current_generation == 0):
                # Initialize the population
                self.initialize_population()
            # First get the fitness of the population
            self.get_population_fitness(self.population.chromosomes)

            #selecion -> crossover -> mutation
            #self.selection_impl(self)
            #self.crossover_impl(self)
            #self.mutation_impl(self)

            #next_population.append(mutated_offspring)

            # Counter for the local number of generations in evolve_generation
            number_of_generations -= 1
            # Add one to the current overall generation
            self.current_generation += 1

    def make_gene(self,value):
        """Let's the user create a gene."""
        return create_gene(value)

    def make_chromosome(self):
        """Let's the user create a chromosome."""
        return create_chromosome()

    def make_population(self):
        """Let's the user create a population."""
        return create_population()
