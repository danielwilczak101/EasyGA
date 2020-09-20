from initialization.random_initialization import random_initialization

def check_gene(value):
    assert value != "" , "Gene can not be empty"
    return value

## Your main structure
class gene:
    # Defults
        # fitness = double , value = Anything
    def __init__(self, value):
        self.fitness = None
        self.value = check_gene(value)

    def get_fitness(self):
        return self.fitness

    def set_fitness(self,fitness):
        self.fitness = fitness

    def get_value(self):
        return self.value

class chromosome:
    # Defults
        # fitness = double, genes = [gene,gene,gene,etc]
    def __init__(self):
        self.fitness = None
        self.genes = []

    def get_fitness(self):
        return self.score

    def add_gene(self,gene):
        self.genes.append(gene)

    def print_chromosome(self):
        for i in range(len(self.genes)):
            print(f"[{self.genes[i].get_value()}],", end = '')


class population:
    # chromosomes = [chromosome,chromosome,etc]
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
