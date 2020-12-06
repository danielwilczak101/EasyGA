# Import math for square root (ga.dist()) and ceil (crossover methods)
import math

# Import random for many methods
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

# Default Attributes for the GA
from attributes import Attributes

# Database class
from database import sql_database
from sqlite3  import Error

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

            # Create the initial population if necessary.
            if self.population is None:
                self.initialize_population()

            # If its the first generation, setup the database.
            if self.current_generation == 0:

                # Create the database here to allow the user to change the
                # database name and structure before running the function.
                self.database.create_all_tables(self)

                # Add the current configuration to the config table
                self.database.insert_config(self)

            # Otherwise evolve the population.
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

            # Adapt the ga if the generation times the adapt rate
            # passes through an integer value.
            adapt_counter = self.adapt_rate*self.current_generation
            if int(adapt_counter) > int(adapt_counter - self.adapt_rate):
                self.adapt()

            number_of_generations -= 1
            self.current_generation += 1


    def evolve(self, number_of_generations = 100, consider_termination = True):
        """Runs the ga until the termination point has been satisfied."""

        while self.active():
            self.evolve_generation(number_of_generations, consider_termination)


    def active(self):
        """Returns if the ga should terminate based on the termination implimented."""

        return self.termination_impl(self)


    def adapt(self):
        """Adapts the ga to hopefully get better results."""

        self.adapt_probabilities()
        self.adapt_population()


    def adapt_probabilities(self):
        """Modifies the parent ratio and mutation rates
        based on the adapt rate and percent converged.
        Attempts to balance out so that a portion of the
        population gradually approaches the solution.
        """

        # Don't adapt
        if self.adapt_probability_rate is None or self.adapt_probability_rate <= 0:
            return

        # Amount of the population desired to converge (default 50%)
        amount_converged = round(self.percent_converged*len(self.population))

        # Difference between best and i-th chromosomes
        best_chromosome = self.population[0]
        tol = lambda i: self.dist(best_chromosome, self.population[i])

        # Change rates with:
        multiplier = 1 + self.adapt_probability_rate

        # Too few converged: cross more and mutate less
        if tol(amount_converged//2) > tol(amount_converged//4)*2:

            self.selection_probability = min(
                self.max_selection_probability,
                self.selection_probability * multiplier
            )

            self.chromosome_mutation_rate = max(
                self.min_chromosome_mutation_rate,
                self.chromosome_mutation_rate / multiplier
            )

            self.gene_mutation_rate = max(
                self.min_gene_mutation_rate,
                self.gene_mutation_rate / multiplier
            )

        # Too many converged: cross less and mutate more
        else:

            self.selection_probability = max(
                self.min_selection_probability,
                self.selection_probability / multiplier
            )

            self.chromosome_mutation_rate = min(
                self.max_chromosome_mutation_rate,
                self.chromosome_mutation_rate * multiplier
            )

            self.gene_mutation_rate = min(
                self.max_gene_mutation_rate,
                self.gene_mutation_rate * multiplier
            )


    def adapt_population(self):
        """
        Performs weighted crossover between the best chromosome and
        the rest of the chromosomes, using negative weights to push
        away chromosomes that are too similar and small positive
        weights to pull in chromosomes that are too different.
        """

        # Don't adapt the population.
        if self.adapt_population_flag == False:
            return

        # Amount of the population desired to converge (default 50%)
        amount_converged = round(self.percent_converged*len(self.population))

        # Difference between best and i-th chromosomes
        best_chromosome = self.population[0]
        tol = lambda i: self.dist(best_chromosome, self.population[i])

        # First non-zero tolerance after amount_converged/4
        for i in range(amount_converged//4, len(self.population)):
            if (tol_i := tol(i)) > 0:
                break

        # First significantly different tolerance
        for j in range(i, len(self.population)):
            if (tol_j := tol(j)) > 2*tol_i:
                break

        # Strongly cross the best chromosome with the worst chromosomes
        for n in range(i, len(self.population)):

            # Strongly cross with the best chromosome
            # May reject negative weight or division by 0
            try:
                self.population[n] = self.crossover_individual_impl(
                    self,
                    self.population[n],
                    best_chromosome,
                    min(0.25, 2 * tol_j / (tol(n) - tol_j))
                )

            # If negative weights can't be used,
            # Cross with j-th chromosome instead
            except:
                self.population[n] = self.crossover_individual_impl(
                    self,
                    self.population[n],
                    self.population[j],
                    0.75
                )

            # Update fitnesses
            self.population[n].fitness = self.fitness_function_impl(self.population[n])

            # Update best chromosome
            if self.target_fitness_type == 'max':
                cond = (self.population[n].fitness > best_chromosome.fitness)

            if self.target_fitness_type == 'min':
                cond = (self.population[n].fitness < best_chromosome.fitness)

            if cond:
                tol_j = tol(j)
                best_chromosome = self.population[n]

        self.population.sort_by_best_fitness(self)


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
        for chromosome in self.population:

            # Update fitness if needed or asked by the user
            if chromosome.fitness is None or self.update_fitness:
                chromosome.fitness = self.fitness_function_impl(chromosome)


    def sort_by_best_fitness(self, chromosome_list, in_place = False):
        """Sorts the chromosome list by fitness based on fitness type.
        1st element has best fitness.
        2nd element has second best fitness.
        etc.
        """

        if in_place:
            chromosome_list.sort(                       # list to be sorted
                key = lambda chromosome: chromosome.fitness,   # by fitness
                reverse = (self.target_fitness_type == 'max')  # ordered by fitness type
            )
            return chromosome_list

        else:
            return sorted(
                chromosome_list,                               # list to be sorted
                key = lambda chromosome: chromosome.fitness,   # by fitness
                reverse = (self.target_fitness_type == 'max')  # ordered by fitness type
            )


    def get_chromosome_fitness(self, index):
        """Returns the fitness value of the chromosome
        at the specified index after conversion based
        on the target fitness type.
        """

        return self.convert_fitness(
            self.population[index].fitness
        )


    def convert_fitness(self, fitness_value):
        """Returns the fitness value if the type of problem
        is a maximization problem. Otherwise the fitness is
        inverted using max - value + min.
        """

        # No conversion needed
        if self.target_fitness_type == 'max': return fitness_value

        max_fitness = self.population[-1].fitness
        min_fitness = self.population[0].fitness

        return max_fitness - fitness_value + min_fitness


    def print_generation(self):
        """Prints the current generation"""
        print(f"Current Generation \t: {self.current_generation}")


    def print_population(self):
        """Prints the entire population"""
        print(self.population)


    def print_best_chromosome(self):
        """Prints the best chromosome and its fitness"""
        print(f"Best Chromosome \t: {self.population[0]}")
        print(f"Best Fitness    \t: {self.population[0].fitness}")


    def print_worst_chromosome(self):
        """Prints the worst chromosome and its fitness"""
        print(f"Worst Chromosome \t: {self.population[-1]}")
        print(f"Worst Fitness    \t: {self.population[-1].fitness}")
