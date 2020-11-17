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

# Default Attributes for the GA
from attributes import Attributes

# Database class
from database import sql_database
from sqlite3 import Error

# Graphing package
from database import matplotlib_graph
import matplotlib.pyplot as plt


class GA(Attributes):
    """GA is the main class in EasyGA. Everything is run through the ga
    class. The GA class inherites all the default ga attributes from the
    attributes class.

    An extensive wiki going over all major functions can be found at
    https://github.com/danielwilczak101/EasyGA/wiki
    """


    def evolve_generation(self, number_of_generations = 1, consider_termination = True):
        """Evolves the ga the specified number of generations."""

        cond1 = lambda: number_of_generations > 0  # Evolve the specified number of generations.
        cond2 = lambda: not consider_termination   # If consider_termination flag is set:
        cond3 = lambda: cond2() or self.active()   #     check termination conditions.

        while cond1() and cond3():
            # If its the first generation
            if self.current_generation == 0:

                # Create the database here to allow the user to change
                # the database name and structure before running the function.
                self.database.create_all_tables(self)
                # Add the current configuration to the config table
                self.database.insert_config(self)
                # Create the initial population
                self.initialize_population()

            # Otherwise evolve the population
            else:
                self.parent_selection_impl(self)
                self.crossover_population_impl(self)
                self.survivor_selection_impl(self)
                self.population.update()
                self.mutation_population_impl(self)

            # Update and sort fitnesses
            self.set_all_fitness()
            self.population.sort_by_best_fitness(self)

            # Save the population to the database
            self.save_population()

            number_of_generations -= 1
            self.current_generation += 1


    def evolve(self):
        """Runs the ga until the termination point has been satisfied."""
        while self.active():
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
            if chromosome.get_fitness() is None or self.update_fitness:
                chromosome.set_fitness(self.fitness_function_impl(chromosome))


    def sort_by_best_fitness(self, chromosome_set):
        """Sorts the array by fitness based on fitness type.
        1st element has best fitness.
        2nd element has second best fitness.
        etc.
        """

        return sorted(
                chromosome_set,                                     # list to be sorted
                key = lambda chromosome: chromosome.get_fitness(),  # by fitness
                reverse = (self.target_fitness_type == 'max')       # ordered by fitness type
            )


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
        if min_fitness / max_fitness < 1e-5:
            return -fitness_value
        else:
            return max_fitness - fitness_value + min_fitness


    def print_generation(self):
        """Prints the current generation"""
        print(f"Current Generation \t: {self.current_generation}")


    def print_population(self):
        """Prints the entire population"""
        print(self.population)


    def print_best(self):
        """Prints the best chromosome and its fitness"""
        print(f"Best Chromosome \t: {self.population.get_chromosome(0)}")
        print(f"Best Fitness    \t: {self.population.get_chromosome(0).get_fitness()}")


    def print_worst(self):
        """Prints the worst chromosome and its fitness"""
        print(f"Worst Chromosome \t: {self.population.get_chromosome(-1)}")
        print(f"Worst Fitness    \t: {self.population.get_chromosome(-1).get_fitness()}")
