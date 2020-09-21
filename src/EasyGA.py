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
        return self.score

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
    def __init__(self, population_size, chromosome_length, user_gene_function):
        # User defined variables
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.user_gene_function = user_gene_function
        # setup required variables
        self.population = []
        # Setup ga implimentation structure
        self.initialization_impl = random_initialization()


    def initialize(self):
        # Create the initial population
        self.population = self.initialization_impl.initialize(self.population_size, self.chromosome_length, self.user_gene_function)
