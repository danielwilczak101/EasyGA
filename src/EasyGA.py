# Import math for square root (ga.dist()) and ceil (crossover methods)
import math

# Import random for many methods
import random

# Import all decorators
import decorators

# Import all the data structure prebuilt modules
from structure import Population as make_population
from structure import Chromosome as make_chromosome
from structure import Gene       as make_gene

# Misc. Methods
from fitness_examples import Fitness_Examples
from termination import Termination

# Parent/Survivor Selection Methods
from parent   import Parent
from survivor import Survivor

# Genetic Operator Methods
from crossover import Crossover
from mutation  import Mutation

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


    def evolve(self, number_of_generations = float('inf'), consider_termination = True):
        """Evolves the ga the specified number of generations
        or until the ga is no longer active if consider_termination is True."""

        # Create the initial population if necessary.
        if self.population is None:
            self.initialize_population()

        cond1 = lambda: number_of_generations > 0  # Evolve the specified number of generations.
        cond2 = lambda: not consider_termination   # If consider_termination flag is set:
        cond3 = lambda: cond2() or self.active()   #     check termination conditions.

        while cond1() and cond3():

            # If its the first generation, setup the database.
            if self.current_generation == 0:

                # Create the database here to allow the user to change the
                # database name and structure before running the function.
                self.database.create_all_tables(self)

                # Add the current configuration to the config table
                self.database.insert_config(self)

            # Otherwise evolve the population.
            else:
                self.parent_selection_impl()
                self.crossover_population_impl()
                self.survivor_selection_impl()
                self.update_population()
                self.sort_by_best_fitness()
                self.mutation_population_impl()

            # Update and sort fitnesses
            self.set_all_fitness()
            self.sort_by_best_fitness()

            # Save the population to the database
            self.save_population()

            # Adapt the ga if the generation times the adapt rate
            # passes through an integer value.
            adapt_counter = self.adapt_rate*self.current_generation
            if int(adapt_counter) < int(adapt_counter + self.adapt_rate):
                self.adapt()

            number_of_generations   -= 1
            self.current_generation += 1


    def update_population(self):
        """Updates the population to the new population and resets the mating pool and new population."""

        self.population.update()


    def reset_run(self):
        """Resets a run by re-initializing the population and modifying counters."""

        self.initialize_population()
        self.current_generation = 0
        self.run += 1


    def active(self):
        """Returns if the ga should terminate based on the termination implimented."""

        return self.termination_impl()


    def adapt(self):
        """Adapts the ga to hopefully get better results."""

        self.adapt_probabilities()
        self.adapt_population()

        # Update and sort fitnesses
        self.set_all_fitness()
        self.sort_by_best_fitness()


    def adapt_probabilities(self):
        """Modifies the parent ratio and mutation rates
        based on the adapt rate and percent converged.
        Attempts to balance out so that a portion of the
        population gradually approaches the solution.
        """

        # Determines how much to adapt by
        weight = self.adapt_probability_rate 

        # Don't adapt
        if weight is None or weight <= 0:
            return

        # Amount of the population desired to converge (default 50%)
        amount_converged = round(self.percent_converged * len(self.population))

        # Difference between best and i-th chromosomes
        best_chromosome = self.population[0]
        tol = lambda i: self.dist(best_chromosome, self.population[i])

        # Too few converged: cross more and mutate less
        if tol(amount_converged//2) > tol(amount_converged//4)*2:
            bounds = (self.max_selection_probability,
                      self.min_chromosome_mutation_rate,
                      self.min_gene_mutation_rate)

        # Too many converged: cross less and mutate more
        else:
            bounds = (self.min_selection_probability,
                      self.max_chromosome_mutation_rate,
                      self.max_gene_mutation_rate)

        # Weighted average of x and y
        average = lambda x, y: weight * x + (1-weight) * y

        # Adjust rates towards the bounds
        self.selection_probability    = average(bounds[0], self.selection_probability)
        self.chromosome_mutation_rate = average(bounds[1], self.chromosome_mutation_rate)
        self.gene_mutation_rate       = average(bounds[2], self.gene_mutation_rate)


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

        self.parent_selection_impl()

        # Strongly cross the best chromosome with all other chromosomes
        for n, parent in enumerate(self.population.mating_pool):

            if self.population[n] != self.population[0]:

                # Strongly cross with the best chromosome
                # May reject negative weight or division by 0
                try:
                    self.crossover_individual_impl(
                        self.population[n],
                        parent,
                        weight = -3/4,
                    )

                # If negative weights can't be used or division by 0, use positive weight
                except ValueError:
                    self.crossover_individual_impl(
                        self.population[n],
                        parent,
                        weight = +1/4,
                    )

            # Stop if we've filled up an entire population
            if len(self.population.next_population) >= len(self.population):
                break

        # Replace worst chromosomes with new chromosomes, except for the previous best chromosome
        min_len = min(len(self.population)-1, len(self.population.next_population))
        if min_len > 0:
            self.population[-min_len:] = self.population.next_population[:min_len]
        self.population.next_population = []
        self.population.mating_pool = []


    def initialize_population(self):
        """Initialize the population using
        the initialization implimentation
        that is currently set.
        """

        if self.chromosome_impl is not None:
            self.population = self.make_population(
                self.chromosome_impl()
                for _
                in range(self.population_size)
            )

        elif self.gene_impl is not None:
            self.population = self.make_population(
                (
                    self.gene_impl()
                    for __
                    in range(self.chromosome_length)
                )
                for _
                in range(self.population_size)
            )

        else:
            raise ValueError("No chromosome or gene impl specified.")


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


    def sort_by_best_fitness(self, chromosome_list = None, in_place = True):
        """Sorts the chromosome list by fitness based on fitness type.
        1st element has best fitness.
        2nd element has second best fitness.
        etc.
        """

        if self.target_fitness_type not in ('max', 'min'):
            raise ValueError("Unknown target fitness type")

        # Sort the population if no chromosome list is given
        if chromosome_list is None:
            chromosome_list = self.population

        # Reversed sort if max fitness should be first
        reverse = (self.target_fitness_type == 'max')

        # Sort by fitness, assuming None should be moved to the end of the list
        key = lambda chromosome: (chromosome.fitness if (chromosome.fitness is not None) else (float('inf') * (+1, -1)[int(reverse)]))

        if in_place:
            chromosome_list.sort(key = key, reverse = reverse)
            return chromosome_list

        else:
            return sorted(chromosome_list, key = key, reverse = reverse)


    def get_chromosome_fitness(self, index):
        """Returns the fitness value of the chromosome
        at the specified index after conversion based
        on the target fitness type.
        """

        return self.convert_fitness(self.population[index].fitness)


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
