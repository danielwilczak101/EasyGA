import EasyGA
import random

# Create the Genetic algorithm
ga = EasyGA.GA()

# Create 25 chromosomes each with 10 genes and 200 generations
ga.population_size = 100
ga.chromosome_length = 10
ga.generation_goal = 150

# Create random genes from 0 to 10
ga.gene_impl = lambda: random.randint(0, 10)

# Minimize the sum of the genes
ga.fitness_function_impl = lambda chromosome: sum(gene.get_value() for gene in chromosome.get_gene_list())
ga.target_fitness_type = 'min'

ga.evolve()

ga.print_generation()
ga.print_population()

ga.graph.type_of_plot = "line"
ga.graph.yscale = "log"
ga.graph.lowest_value_chromosome()
