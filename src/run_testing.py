import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

# Create 25 chromosomes each with 10 genes
ga.population_size = 25
ga.chromosome_length = 10

# Create random genes from 0 to 10
ga.gene_impl = lambda: random.randint(0, 10)

# Minimize the sum of the genes
ga.fitness_function_impl = lambda chromosome: sum(gene.get_value() for gene in chromosome.get_gene_list())
ga.target_fitness_type = 'min'

# Terminate when a chromosome has all 0's
ga.fitness_goal = 0
ga.termination_impl = EasyGA.Termination_Methods.fitness_based

ga.evolve()

print(f"Current Generation: {ga.current_generation}")
ga.population.print_all()
