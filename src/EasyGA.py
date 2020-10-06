import random
# Import all the data structure prebuilt modules
from initialization import population as create_population
from initialization import chromosome as create_chromosome
from initialization import gene as create_gene
# Import example classes
from fitness_function import fitness_examples
from initialization import initialization_examples
from termination_point import termination_examples
from selection import selection_examples
from crossover import crossover_examples
from repopulate import repopulate_examples
from mutation import mutation_examples

class GA:
    def __init__(self):
        """Initialize the genetic algorithm. Where all the hyper parmeters are
        set for the the ga to function."""
        # Initilization variables
        self.chromosome_length  = 3
        self.population_size    = 10
        self.chromosome_impl    = None
        self.gene_impl          = None
        self.population         = None
        # Termination varibles
        self.current_generation = 0
        self.current_fitness    = 0
        self.generation_goal    = 0
        self.fitness_goal       = 4
        # Mutation variables
        self.mutation_rate      = 0.02

        # Rerun already computed fitness
        self.update_fitness     = False

        # Defualt EastGA implimentation structure
        self.initialization_impl   = initialization_examples.random_initialization
        self.fitness_funciton_impl = fitness_examples.is_it_5
        self.selection_impl   = selection_examples.roulette
        self.crossover_impl   = crossover_examples.single_point_crossover
        self.repopulate_impl  = repopulate_examples.kill_two_worst
        self.mutation_impl    = mutation_examples.per_gene_mutation
        self.termination_impl = termination_examples.generation_based

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
            chromosome.set_fitness(self.fitness_funciton_impl(chromosome))


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
        """Evolves the ga the specified number of generations."""
        while(number_of_generations > 0):
            # If its the first generation then initialize the population
            if(self.current_generation == 0):
                # Initialize the population
                self.initialize_population()
            # First get the fitness of the population
            self.get_population_fitness(self.population.chromosome_list)


            """A new population is created every generation"""
            # Selection - Triggers flags in the chromosome if its been selected
            self.selection_impl(self)
            # Crossover - Takes the flagged chromosomes and crosses there genetic
            # makup to make new offsprings.
            self.crossover_impl(self)
            # Repopulate - Manipulates the population to some desired way  Ex. Elitism
            self.repopulate_impl(self)
            # Mutation - Manipulates the population very slightly
            self.mutation_impl(self)

            # Print the current generation number
            print()
            print(f"Generation - {self.current_generation}")
            # Print the current population
            self.population.print_all()

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
