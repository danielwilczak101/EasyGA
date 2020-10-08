import random
# Import all the data structure prebuilt modules
from initialization import Population as create_population
from initialization import Chromosome as create_chromosome
from initialization import Gene as create_gene
# Structure Methods
from fitness_function import Fitness_Examples
from initialization import Initialization_Methods
from termination_point import Termination_Methods
# Population Methods
from survivor_selection import Survivor_Selection
from parent_selection import Parent_Selection
# Manipulation Methods
from mutation import Mutation_Methods
from crossover import Crossover_Methods

class GA:
    def __init__(self):
        """Initialize the GA."""
        # Initilization variables
        self.chromosome_length = 10
        self.population_size = 150
        self.chromosome_impl = None
        self.gene_impl = None
        self.population = None
        self.target_fitness_type = 'maximum'
        self.update_fitness = True

        # Selection variables
        self.parent_ratio = 0.1
        self.selection_probability = 0.95

        # Termination variables
        self.current_generation = 0
        self.current_fitness = 0

        self.generation_goal = 250
        self.fitness_goal = 9

        # Mutation variables
        self.mutation_rate = 0.10

        # Default EasyGA implimentation structure
        self.initialization_impl = Initialization_Methods.random_initialization
        self.fitness_function_impl = Fitness_Examples.index_dependent_values
        # Selects which chromosomes should be automaticly moved to the next population
        self.survivor_selection_impl = Survivor_Selection.remove_two_worst
        # Methods for accomplishing parent-selection -> Crossover -> Mutation
        self.parent_selection_impl = Parent_Selection.Tournament.with_replacement
        self.crossover_impl = Crossover_Methods.single_point_crossover
        self.mutation_impl = Mutation_Methods.per_gene_mutation
        # The type of termination to impliment
        self.termination_impl = Termination_Methods.generation_based


    def evolve_generation(self, number_of_generations = 1, consider_termination = True):
        """Evolves the ga the specified number of generations."""
        while(number_of_generations > 0 and (consider_termination == False or self.termination_impl(self))):
            # If its the first generation then initialize the population
            if self.current_generation == 0:
                self.initialize_population()
                self.set_all_fitness(self.population.chromosome_list)
                self.population.set_all_chromosomes(self.sort_by_best_fitness())
            else:
                self.parent_selection_impl(self)
                next_population = self.crossover_impl(self)
                next_population = self.survivor_selection_impl(self, next_population)
                next_population.set_all_chromosomes(self.mutation_impl(self, next_population.get_all_chromosomes()))

                self.population = next_population
                self.set_all_fitness(self.population.chromosome_list)
                self.population.set_all_chromosomes(self.sort_by_best_fitness())

            number_of_generations -= 1

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

    def sort_by_best_fitness(self, chromosome_set = None):

        if chromosome_set == None:
            chromosome_set = self.population.get_all_chromosomes()

        chromosome_set_temp = chromosome_set
        not_sorted_check = 0
        while (not_sorted_check != len(chromosome_set_temp)):
            not_sorted_check = 0
            for i in range(len(chromosome_set_temp)):
                if ((i + 1 < len(chromosome_set_temp)) and (chromosome_set_temp[i + 1].fitness > chromosome_set_temp[i].fitness)):
                    temp = chromosome_set[i]
                    chromosome_set_temp[i] = chromosome_set[i + 1]
                    chromosome_set_temp[i + 1] = temp
                else:
                    not_sorted_check += 1

        chromosome_set = chromosome_set_temp

        return chromosome_set

    def make_gene(self,value):
        """Let's the user create a gene."""
        return create_gene(value)

    def make_chromosome(self):
        """Let's the user create a chromosome."""
        return create_chromosome()

    def make_population(self):
        """Let's the user create a population."""
        return create_population()
