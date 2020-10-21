import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()
ga.target_fitness_type = 'min'
ga.chromosome_length = 10
ga.population_size = 25
ga.generation_goal = 50
ga.gene_impl = lambda: random.randint(0, 10)

def fitness_function(chromosome):
    return sum(
               gene.get_value()
           for gene in chromosome.get_gene_list())

ga.fitness_function_impl = fitness_function

ga.evolve()
ga.set_all_fitness()
ga.population.sort_by_best_fitness(ga)

print(f"Current Generation: {ga.current_generation}")
ga.population.print_all()
