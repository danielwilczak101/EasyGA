import random
# Import all the data structure prebuilt modules
from initialization import Population as create_population
from initialization import Chromosome as create_chromosome
from initialization import Gene as create_gene
# Import example classes
from fitness_function import Fitness_Examples
from initialization import Initialization_Types
from termination_point import Termination_Types
from selection import Selection_Types
from crossover import Crossover_Types
from mutation import Mutation_Types

class GA:
    def __init__(self):
        """Initialize the GA."""
        # Initilization variables
        self.chromosome_length = 10
        self.population_size = 100
        self.chromosome_impl = None
        self.gene_impl = None
        self.population = None
        # Termination varibles
        self.current_generation = 0
        self.current_fitness = 0
        self.generation_goal = 50
        self.fitness_goal = 3
        # Mutation variables
        self.mutation_rate = 0.05

        # Rerun already computed fitness
        self.update_fitness = True

        # Defualt EastGA implimentation structure
        self.initialization_impl = Initialization_Types().random_initialization
        self.fitness_function_impl = Fitness_Examples().is_it_5
        self.mutation_impl = Mutation_Types().random_mutation
        self.selection_impl = Selection_Types().Tournament().with_replacement
        self.crossover_impl = Crossover_Types().single_point_crossover
        self.termination_impl = Termination_Types().generation_based

    def initialize_population(self):
        """Initialize the population using the initialization
         implimentation that is currently set"""
        self.population = self.initialization_impl(self)
        
    def set_all_fitness(self,chromosome_set):
        """Will get and set the fitness of each chromosome in the population.
        If update_fitness is set then all fitness values are updated.
        Otherwise only fitness values set to None (i.e. uninitialized
        fitness values) are updated."""
        # Get each chromosome in the population

        for chromosome in chromosome_set:
            if(chromosome.fitness == None or self.update_fitness == True):
                # Set the chromosomes fitness using the fitness function
                chromosome.set_fitness(self.fitness_function_impl(chromosome))

    def evolve(self):
        """Runs the ga until the termination point has been satisfied."""
        # While the termination point hasnt been reached keep running
        while(self.active()):
            self.evolve_generation()

    def evolve_generation(self, number_of_generations = 1, consider_termination = True):
        """Evolves the ga the specified number of generations."""
        while(number_of_generations > 0 and (consider_termination == False or self.termination_impl(self))):
            # If its the first generation then initialize the population
            if self.current_generation == 0:
                self.initialize_population()
                self.set_all_fitness(self.population.chromosomes)
            
            next_population = self.selection_impl(self)
            self.population = next_population
            self.set_all_fitness(self.population.chromosomes)

            number_of_generations -= 1
            self.current_generation += 1

    def active(self):
        """Returns if the ga should terminate base on the termination implimented"""
        return self.termination_impl(self)

    def make_gene(self,value):
        return create_gene(value)

    def make_chromosome(self):
        return create_chromosome()

    def make_population(self):
        return create_population()
