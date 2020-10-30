import random
import EasyGA

# Create the Genetic algorithm
#   Reproduce 30% of the population.
#   Mutate 20% of the population.
#   Mutate 3% of the genes in each mutated chromosome.
#   
#   Create 100 chromosomes each with 25 genes
#   Create random genes from 0 to 10
#   
#   Minimize the sum of the genes
#   Terminate when a chromosome has all 0's
#     or 150 generations pass
# 
ga = EasyGA.GA(
    parent_ratio = 0.30,
    chromosome_mutation_rate = 0.20,
    gene_mutation_rate = 0.03,
    population_size = 100,
    chromosome_length = 25,
    gene_impl = lambda: random.randint(0, 10),
    fitness_function_impl = lambda chromosome: sum(gene.get_value() for gene in chromosome.get_gene_list()),
    target_fitness_type = 'min',
    fitness_goal = 0,
    generation_goal = 150
)

# Run 10 generations at a time
while ga.active():
    ga.evolve_generation(10)
    ga.print_generation()
    ga.print_best()
    #ga.print_population()
    print('-'*75)
