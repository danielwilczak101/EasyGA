import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

# Reproduce 30% of the population.
# Mutate 20% of the population.
# Mutate 3% of the genes in each mutated chromosome.
ga.parent_ratio  = 0.30
ga.chromosome_mutation_rate = 0.20
ga.gene_mutation_rate = 0.03

# Create 25 chromosomes each with 10 genes
ga.population_size = 100
ga.chromosome_length = 25

# Create random genes from 0 to 10
ga.gene_impl = lambda: random.randint(0, 10)

# Minimize the sum of the genes
ga.fitness_function_impl = lambda chromosome: sum(gene.get_value() for gene in chromosome.get_gene_list())
ga.target_fitness_type = 'min'

# Terminate when a chromosome has all 0's
ga.fitness_goal = 0
ga.generation_goal = 150

while ga.active():
    ga.evolve_generation(10)
    ga.print_generation()
    ga.print_best()
    #ga.print_population()
    print('-'*75)
