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

from attributes import attributes


class GA(attributes):

    # Inhert all the ga attributes from the attributes class.
    def __init__(self):             
       super(GA, self).__init__()


    def evolve_generation(self, number_of_generations = 1, consider_termination = True):
        """Evolves the ga the specified number of generations."""

        while(number_of_generations > 0      # Evolve the specified number of generations
              and (not consider_termination  #     and if consider_termination flag is set
                   or self.active())):       #         then also check if termination conditions reached

            # If its the first generation then initialize the population
            if self.current_generation == 0:
                self.initialize_population()
                self.set_all_fitness()
                self.population.sort_by_best_fitness(self)

            # Otherwise evolve the population
            else:
                self.parent_selection_impl(self)
                self.crossover_population_impl(self)
                self.survivor_selection_impl(self)
                self.mutation_population_impl(self)
                self.population.update()
                self.set_all_fitness()
                self.population.sort_by_best_fitness(self)

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
                     reverse = (self.target_fitness_type == 'max'))      # from highest to lowest fitness


    def get_chromosome_fitness(self, index):
        """Returns the fitness value of the chromosome
        at the specified index after conversion based
        on the target fitness type.
        """
        return self.convert_fitness(
                   self.population.get_chromosome(index).get_fitness()
               )


    def convert_fitness(self, fitness_value):
        """Returns the fitness value if the type of problem
        is a maximization problem. Otherwise the fitness is
        inverted using max - value + min.
        """

        if self.target_fitness_type == 'max': return fitness_value
        max_fitness = self.population.get_chromosome(-1).get_fitness()
        min_fitness = self.population.get_chromosome(0).get_fitness()
        return max_fitness - fitness_value + min_fitness


    def print_generation(self):
        """Prints the current generation"""
        print(f"Current Generation \t: {self.current_generation}")


    def print_population(self):
        """Prints the entire population"""
        self.population.print_all()


    def print_best(self):
        """Prints the best chromosome and its fitness"""
        print(f"Best Chromosome \t: {self.population.get_chromosome(0)}")
        print(f"Best Fitness    \t: {self.population.get_chromosome(0).get_fitness()}")
