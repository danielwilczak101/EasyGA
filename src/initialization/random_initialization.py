from initialization.population import population
from initialization.chromosome import chromosome
from initialization.gene import gene

from initialization.initialization import initialization

class random_initialization(initialization):
    def initialize(self,chromosome_length,population_size,gene_function):
        # Create the population object
        population = population.population()
        # Fill the population with chromosomes
        for i in range(population_size):
            chromosome = chromosome.chromosome()
            #Fill the Chromosome with genes
            for j in range(chromosome_length):
                gene = gene.gene(gene_function)
                chromosome.add_gene(gene)

            population.add_chromosome(chromosome)
        return population
