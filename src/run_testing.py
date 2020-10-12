import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

ga.population_size = 100
ga.chromosome_length = 10
ga.generation_goal =  100
ga.gene_impl = [random.randint,1,10]
ga.parent_selection_impl = EasyGA.Parent_Selection.Roulette.roulette_selection

ga.evolve()

ga.population.print_all()
