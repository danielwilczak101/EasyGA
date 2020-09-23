from population import population
from chromosome import chromosome
from gene import gene

population = population()
# Fill the population with chromosomes
for i in range(population_size):
    chromosome = chromosome()
    #Fill the Chromosome with genes
    for j in range(chromosome_length):
        gene = gene(gene_function)
        chromosome.add_gene(gene)

    population.add_chromosome(chromosome)
