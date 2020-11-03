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
from attributes import attributes


class GA(attributes):
    """GA is the main class in EasyGA. Everything is run through the ga
    class. The GA class inherites all the default ga attributes from the
    attributes class.

    An extensive wiki going over all major functions can be found at
    https://github.com/danielwilczak101/EasyGA/wiki
    """

    def __init__(self,
            chromosome_length = None,
            population_size = None,
            chromosome_impl = None,
            gene_impl = None,
            population = None,
            target_fitness_type = None,
            update_fitness = None,
            parent_ratio = None,
            selection_probability = None,
            tournament_size_ratio = None,
            current_generation = None,
            current_fitness = None,
            generation_goal = None,
            fitness_goal = None,
            chromosome_mutation_rate = None,
            gene_mutation_rate = None,
            initialization_impl = None,
            fitness_function_impl = None,
            make_population = None,
            make_chromosome = None,
            make_gene = None,
            parent_selection_impl = None,
            crossover_individual_impl = None,
            crossover_population_impl = None,
            survivor_selection_impl = None,
            mutation_individual_impl = None,
            mutation_population_impl = None,
            termination_impl = None
            ):
        super(GA, self).__init__(
            chromosome_length,
            population_size,
            chromosome_impl,
            gene_impl,
            population,
            target_fitness_type,
            update_fitness,
            parent_ratio,
            selection_probability,
            tournament_size_ratio,
            current_generation,
            current_fitness,
            generation_goal,
            fitness_goal,
            chromosome_mutation_rate,
            gene_mutation_rate,
            initialization_impl,
            fitness_function_impl,
            make_population,
            make_chromosome,
            make_gene,
            parent_selection_impl,
            crossover_individual_impl,
            crossover_population_impl,
            survivor_selection_impl,
            mutation_individual_impl,
            mutation_population_impl,
            termination_impl
        )


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
                self.population.update()
                self.mutation_population_impl(self)
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
