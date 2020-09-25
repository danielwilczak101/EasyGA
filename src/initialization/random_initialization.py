# Import the data structure
from .population_structure.population import population as create_population
from .chromosome_structure.chromosome import chromosome as create_chromosome
from .gene_structure.gene import gene as create_gene
from .gene_function.gene_random import random_gene as random_gene

def random_initialization(chromosome_length,population_size,gene_function,gene_input,gene_input_type):

    if gene_function == random_gene:
        # Create the population object
        population = create_population()
        # Fill the population with chromosomes
        for i in range(population_size):
            chromosome = create_chromosome()
            #Fill the Chromosome with genes
            for j in range(chromosome_length):
                chromosome.add_gene(create_gene(gene_function(gene_input, gene_input_type, j)))
            population.add_chromosome(chromosome)
        return population

    else: #For user input gene-function, don't do anything with gene_input parameter
        # Create the population object
        population = create_population()
        # Fill the population with chromosomes
        for i in range(population_size):
            chromosome = create_chromosome()
            #Fill the Chromosome with genes
            for j in range(chromosome_length):
                chromosome.add_gene(create_gene(gene_function()))
            population.add_chromosome(chromosome)
        return population