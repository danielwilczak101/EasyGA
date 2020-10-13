import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()
ga.population_size = 100
ga.generation_goal = 200
ga.parent_selection_impl     = EasyGA.Parent_Selection.Roulette.stochastic_selection
ga.crossover_population_impl = EasyGA.Crossover_Methods.Population.sequential_selection
ga.survivor_selection_impl   = EasyGA.Survivor_Selection.fill_in_parents_then_random

ga.evolve()
ga.set_all_fitness()
ga.population.set_all_chromosomes(ga.sort_by_best_fitness(ga.population.get_all_chromosomes()))

print(f"Current Generation: {ga.current_generation}")
ga.population.print_all()
