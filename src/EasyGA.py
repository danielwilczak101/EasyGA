import random

# Import all the data prebuilt modules
from initialization import population as create_population
from initialization import chromosome as create_chromosome
from initialization import gene as create_gene

# Import functionality defaults
from initialization import random_initialization

class GA:
    def __init__(self):
        """Initialize the GA."""

        # Default variables
        self.chromosome_impl = None
        self.gene_impl = None
        self.population = None
        self.current_generation = 0
        self.generations = 3
        self.chromosome_length = 3
        self.population_size = 5
        self.mutation_rate = 0.03

        # Defualt EastGA implimentation structure
        self.initialization_impl = random_initialization
        self.update_fitness = True
        #self.mutation_impl = PerGeneMutation(Mutation_rate)
        #self.selection_impl = TournamentSelection()
        #self.crossover_impl = FastSinglePointCrossover()
        #self.termination_impl = GenerationTermination(Total_generations)
        #self.evaluation_impl = TestEvaluation()

    def initialize_population(self):
        """Initialize the population"""
        self.population = self.initialization_impl(
        self.population_size,
        self.chromosome_length,
        self.chromosome_impl,
        self.gene_impl)

    def fitness_impl(self, chromosome):
        """Returns the fitness of a chromosome"""
        pass

    def evolve(self):
        """Runs the ga until the ga is no longer active."""

        # run one iteration while the ga is active
        while self.active():
            self.evolve_generation(1)

    def active(self):
        """Returns if the ga should terminate or not"""
        return self.current_generation < self.generations

    def evolve_generation(self, number_of_generations):
        """Evolves the ga the specified number of generations.
        If update_fitness is set then all fitness values are updated.
        Otherwise only fitness values set to None (i.e. uninitialized fitness values) are updated."""

        # run the specified number of times
        for n in range(number_of_generations):

            # for each chromosome in the population
            for chromosome in self.population.get_all_chromosomes():

                # if the fitness should be updated, update it
                if self.update_fitness or chromosome.get_fitness() is None:
                    chromosome.set_fitness(self.fitness_impl(chromosome))

            # apply selection, crossover, and mutation

    def make_gene(self,value):
        """Let's the user create a gene."""
        return create_gene(value)

    def make_chromosome(self):
        """Let's the user create a chromosome."""
        return create_chromosome()

    def make_population(self):
        """Let's the user create a population."""
        return create_population()
