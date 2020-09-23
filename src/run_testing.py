import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()


def user_initialize():

    population_size = 1
    chromosome_length = 3

    population = ga.make_population()
    # Fill the population with chromosomes
    for i in range(population_size):
        chromosome = ga.make_chromosome()
        #Fill the Chromosome with genes
        for j in range(chromosome_length):
            chromosome.add_gene(ga.make_gene("hello"))
        population.add_chromosome(chromosome)
    return population


# Start the population
ga.initialization_impl = user_initialize()

#make gene
new_gene = ga.make_gene("Hello")
print(new_gene.get_value())
print(new_gene.get_fitness())

print(ga.population)

for chromosome in ga.population.chromosomes:
    print(chromosome.genes[0].__dict__)
