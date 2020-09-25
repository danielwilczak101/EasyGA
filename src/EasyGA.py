# Import all the data prebuilt modules
from initialization.population_structure.population import population as create_population
from initialization.chromosome_structure.chromosome import chromosome as create_chromosome
from initialization.gene_structure.gene import gene as create_gene

# Import functions for defaults
from initialization.gene_function.gene_random import random_gene
# Import functionality defaults
from initialization.random_initialization import random_initialization


class GA:
    def __init__(self):
        # Default variables
        self.population = None
        self.generations = 3
        self.chromosome_length = 4
        self.population_size = 5
        self.mutation_rate = 0.03
        # Defualt EastGA implimentation structure
        self.gene_function_impl = random_gene
        # Set the GA Configuration
        self.initialization_impl = random_initialization
        #self.mutation_impl = PerGeneMutation(Mutation_rate)
        #self.selection_impl = TournamentSelection()
        #self.crossover_impl = FastSinglePointCrossover()
        #self.termination_impl = GenerationTermination(Total_generations)
        #self.evaluation_impl = TestEvaluation()


    def initialize(self):
        # Create the first population
        self.population = self.initialization_impl(
        self.population_size,
        self.chromosome_length,
        self.gene_function_impl)

    def evolve():
        # If you just want to evolve through all generations
        pass

    def evolve_generation(self, number_of_generations):
        # If you want to evolve through a number of generations
        # and be able to pause and output data based on that generation run.
        pass

    def make_gene(self,value):
        return create_gene(value)

    def make_chromosome(self):
        return create_chromosome()

    def make_population(self):
        return create_population()
