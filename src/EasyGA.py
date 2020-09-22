# Defult packages for GA functionality
from initialization.random_initialization import random_initialization

def check_gene(value):
    #Check to make sure the gene is not empty
    assert value != "" , "Gene can not be empty"
    return value

## Your main structure
class gene:
    # Defults
        # fitness = Anything, value = Anything
    def __init__(self, value):
        self.fitness = None
        self.value = check_gene(value)

    def set_fitness(self,fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

    def get_value(self):
        return self.value

    def print_value(self):
        print(self.value)

    def print_fitness(self):
        print(self.fitness)

class chromosome:
    # Defults
        # fitness = Anything, genes = [gene,gene,gene,etc]
    def __init__(self):
        self.fitness = None
        self.genes = []

    def add_gene(self,gene):
        self.genes.append(gene)

    def get_fitness(self):
        return self.fitness

    def get_chromosome(self):
        return self.genes

    def print_chromosome(self):
        for i in range(len(self.genes)):
            # Print the gene one by one.
            if(i == len(self.genes) - 1):
                print(f"[{self.genes[i].get_value()}]")
            else:
                print(f"[{self.genes[i].get_value()}],", end = '')

class population:
    # population = [chromosome,chromosome,etc]
    def __init__(self):
        self.chromosomes = []

    def add_chromosome(self,chromosome):
        self.chromosomes.append(chromosome)

class GA:
    def __init__(self):
        # Default variables
        self.population_size = defaults.generations
        self.chromosome_length = defaults.chromosome_length
        self.generations = defaults.generations
        # Defualt ga implimentation structure
        self.create_gene = defaults.default_gene_function()
        self.initialization = defaults.default_initialize()
        self.mutation = defaults.default_mutations_function()
        self.selection = defaults.default_selection_function()
        self.crossover = defaults.default_crossover_function()
        self.termination = defaults.default_termination_function(self.generations)
        self.fitness_function = defaults.default_fitness_function()

    def initialize(self):
        # Create the initial population
        self.population = self.initialization.initialize(self.population_size,
                                                                self.chromosome_length,
                                                                 self.user_gene_function)

    def evolve(self):
        # Evolve will run all the functions
        initialize()


class defaults(self):

    def __init__(self):
        self.generations = 3
        self.chromosome_length = 4
        self.population_size = 5
        self.mutation_rate = 0.03

    def default_gene_function():
        return random.randint(1, 100)

    def default_fitness_function():
        pass

    def default_initialize_functio():
        return random_initialization()

    def default_selection_function():
        return tournament_selection()

    def default_crossover_function():
        return fast_single_point_crossover()

    def default_mutations_function():
        return per_gene_mutation()

    def default_termination_function(generations):
        return generation_termination(generations)
