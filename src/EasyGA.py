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

class GA:

    def __init__(self):
        """Initialize the GA."""

        # Initilization variables
        self.chromosome_length   = 10
        self.population_size     = 10
        self.chromosome_impl     = None
        self.gene_impl           = None
        self.population          = None
        self.target_fitness_type = 'maximum'
        self.update_fitness      = True

        # Selection variables
        self.parent_ratio          = 0.1
        self.selection_probability = 0.75
        self.tournament_size_ratio = 0.1

        # Termination variables
        self.current_generation = 0
        self.current_fitness    = 0
        self.generation_goal    = 15
        self.fitness_goal       = 9

        # Mutation variables
        self.mutation_rate = 0.10

        # Default EasyGA implimentation structure
        self.initialization_impl   = Initialization_Methods.random_initialization
        self.fitness_function_impl = Fitness_Examples.is_it_5
        self.make_population       = create_population
        self.make_chromosome       = create_chromosome
        self.make_gene             = create_gene

        # Methods for accomplishing Parent-Selection -> Crossover -> Survivor_Selection -> Mutation
        self.parent_selection_impl     = Parent_Selection.Tournament.with_replacement
        self.crossover_individual_impl = Crossover_Methods.Individual.single_point
        self.crossover_population_impl = Crossover_Methods.Population.random_selection
        self.survivor_selection_impl   = Survivor_Selection.fill_in_best
        self.mutation_individual_impl  = Mutation_Methods.Individual.single_gene
        self.mutation_population_impl  = Mutation_Methods.Population.random_selection

        # The type of termination to impliment
        self.termination_impl = Termination_Methods.generation_based


    def evolve_generation(self, number_of_generations = 1, consider_termination = True):
        """Evolves the ga the specified number of generations."""

        while(number_of_generations > 0               # Evolve the specified number of generations
              and (not consider_termination           #     and if consider_termination flag is set
                   or self.termination_impl(self))):  #         then also check if termination conditions reached

            # If its the first generation then initialize the population
            if self.current_generation == 0:
                self.initialize_population()
                self.set_all_fitness()
                self.population.sort_by_best_fitness(self)

            # Otherwise evolve the population
            else:
                self.set_all_fitness()
                self.population.sort_by_best_fitness(self)
                self.parent_selection_impl(self)
                self.crossover_population_impl(self)
                self.survivor_selection_impl(self)
                self.mutation_population_impl(self)
                self.population.update()

            number_of_generations -= 1
            self.current_generation += 1


    def evolve(self):
        """Runs the ga until the termination point has been satisfied."""
        while(self.active()):
            self.evolve_generation()


    def active(self):
        """Returns if the ga should terminate based on the termination implimented."""
        return self.termination_impl(self)


    def initialize_population(self):
        """Initialize the population using
        the initialization implimentation
        that is currently set.
        """
        self.population = self.initialization_impl(self)


    def set_all_fitness(self):
        """Will get and set the fitness of each chromosome in the population.
        If update_fitness is set then all fitness values are updated.
        Otherwise only fitness values set to None (i.e. uninitialized
        fitness values) are updated.
        """

        # Check each chromosome
        for chromosome in self.population.get_chromosome_list():

            # Update fitness if needed or asked by the user
            if(chromosome.get_fitness() is None or self.update_fitness):
                chromosome.set_fitness(self.fitness_function_impl(chromosome))


    def sort_by_best_fitness(self, chromosome_set):
        """Sorts the array by fitness.
        1st element has highest fitness.
        2nd element has second highest fitness.
        etc.
        """

        return sorted(chromosome_set,                                    # list to be sorted
                     key = lambda chromosome: chromosome.get_fitness(),  # by fitness
                     reverse = True)                                     # from highest to lowest fitness
