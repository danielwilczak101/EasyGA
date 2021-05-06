from __future__ import annotations
from typing import Optional, MutableSequence, Iterable

# Import all decorators
import decorators

# Import all the data structure prebuilt modules
from structure import Population as make_population
from structure import Chromosome as make_chromosome
from structure import Gene       as make_gene
from structure import Population
from structure import Chromosome
from structure import Gene

# Misc. Methods
from examples import Fitness
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
    """
    GA is the main controller class for EasyGA. Everything is run
    through the GA class. The GA class inherits all default attributes
    from the Attributes dataclass.

    An extensive wiki going over all major functionalities can be found at
    https://github.com/danielwilczak101/EasyGA/wiki
    """


    def evolve(self: GA, number_of_generations: float = float('inf'), consider_termination: bool = True) -> None:
        """
        Evolves the ga until the ga is no longer active.

        Parameters
        ----------
        number_of_generations : float = inf
            The number of generations before the GA terminates. Runs forever by default.
        consider_termination : bool = True
            Whether GA.active() is checked for termination.
        """

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


    def update_population(self: GA) -> None:
        """
        Updates the population to the new population
        and resets the mating pool and new population.
        """
        self.population.update()


    def reset_run(self: GA) -> None:
        """
        Resets a run by re-initializing the
        population and modifying counters.
        """
        self.initialize_population()
        self.current_generation = 0
        self.run += 1


    def adapt(self: GA) -> None:
        """Adapts the ga to hopefully get better results."""

        self.adapt_probabilities()
        self.adapt_population()

        # Update and sort fitnesses
        self.set_all_fitness()
        self.sort_by_best_fitness()


    def adapt_probabilities(self: GA) -> None:
        """
        Modifies the parent ratio and mutation rates based on the adapt
        rate and percent converged. Attempts to balance out so that a
        portion of the population gradually approaches the solution.
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


    def adapt_population(self: GA) -> None:
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


    def initialize_population(self: GA) -> None:
        """
        Sets self.population using the chromosome implementation and population size.
        """
        self.population = self.make_population(self.population_impl())


    def set_all_fitness(self: GA) -> None:
        """
        Sets the fitness of each chromosome in the population.

        Attributes
        ----------
        update_fitness : bool
            Whether fitnesses are recalculated even if they were previously calculated.
            Allows chromosomes which exist in dynamic environments.
        fitness_function_impl(chromosome) -> float
            The fitness function which measures how well a chromosome is doing.
        """

        # Check each chromosome
        for chromosome in self.population:

            # Update fitness if needed or asked by the user
            if chromosome.fitness is None or self.update_fitness:
                chromosome.fitness = self.fitness_function_impl(chromosome)


    def sort_by_best_fitness(
            self: GA,
            chromosome_list: Optional[
                Union[MutableSequence[Chromosome],
                Iterable[Chromosome]]
                ] = None,
            in_place: bool = True,
        ) -> MutableSequence[Chromosome]:
        """
        Sorts the chromosome list by fitness based on fitness type.
        1st element has best fitness.
        2nd element has second best fitness.
        etc.

        Parameters
        ----------
        chromosome_list : MutableSequence[Chromosome] = self.population
            The list of chromosomes to be sorted. By default, the population is used.
            May be sorted in-place.
        chromosome_list : Iterable[Chromosome]
            The list of chromosomes to be sorted. By default, the population is used.
            May not be sorted in-place.
        in_place : bool = True
            Whether the sort is done in-place, modifying the original object, or not.

        Attributes
        ----------
        target_fitness_type : str in ('max', 'min')
            The way the chromosomes should be sorted.

        Returns
        -------
        chromosome_list : MutableSequence[Chromosome]
            The sorted chromosomes.
        """

        if self.target_fitness_type not in ('max', 'min'):
            raise ValueError("Unknown target fitness type")

        # Sort the population if no chromosome list is given
        if chromosome_list is None:
            chromosome_list = self.population

        # Reversed sort if max fitness should be first
        reverse = (self.target_fitness_type == 'max')

        # Sort by fitness, assuming None should be moved to the end of the list
        def key(chromosome):
            if chromosome.fitness is not None:
                return chromosome.fitness
            elif reverse:
                return float('-inf')
            else:
                return float('inf')

        if in_place:
            chromosome_list.sort(key=key, reverse=reverse)
            return chromosome_list

        else:
            return sorted(chromosome_list, key=key, reverse=reverse)


    def get_chromosome_fitness(self: GA, index: int) -> float:
        """
        Computes the converted fitness of a chromosome at an index.
        The converted fitness remaps the fitness to sensible values
        for various methods.

        Parameters
        ----------
        index : int
            The index of the chromosome in the population.

        Attributes
        ----------
        convert_fitness(float) -> float
            A method for redefining the fitness value.

        Returns
        -------
        fitness : float
            The converted fitness value.
        """
        return self.convert_fitness(self.population[index].fitness)


    def convert_fitness(self: GA, fitness: float) -> float:
        """
        Calculates a modified version of the fitness for various
        methods, which assume the fitness should be maximized.

        Parameters
        ----------
        fitness : float
            The fitness value to be changed.

        Attributes
        ----------
        target_fitness_type : str in ('max', 'min')
            The way the chromosomes should be sorted.

        Returns
        -------
        fitness : float
            Unchanged if the fitness is already being maximized.
        max_fitness - fitness + min_fitness : float
            The fitness flipped if the fitness is being minimized.

        Requires
        --------
        The population must be sorted already, and the fitnesses can't be None.
        """

        # No conversion needed
        if self.target_fitness_type == 'max':
            return fitness

        max_fitness = self.population[-1].fitness
        min_fitness = self.population[0].fitness

        return max_fitness - fitness + min_fitness


    def print_generation(self: GA) -> None:
        """Prints the current generation."""
        print(f"Current Generation \t: {self.current_generation}")


    def print_population(self: GA) -> None:
        """Prints the entire population."""
        print(self.population)


    def print_best_chromosome(self: GA) -> None:
        """Prints the best chromosome and its fitness."""
        print(f"Best Chromosome \t: {self.population[0]}")
        print(f"Best Fitness    \t: {self.population[0].fitness}")


    def print_worst_chromosome(self: GA) -> None:
        """Prints the worst chromosome and its fitness."""
        print(f"Worst Chromosome \t: {self.population[-1]}")
        print(f"Worst Fitness    \t: {self.population[-1].fitness}")
