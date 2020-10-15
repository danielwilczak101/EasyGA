import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()
ga.population_size = 100
ga.generation_goal = 100
ga.gene_impl       = lambda: random.randint(1, 10)
ga.selection_probability = 0.5
ga.fitness_function_impl     = EasyGA.Fitness_Examples.near_5
ga.parent_selection_impl     = EasyGA.Parent_Selection.Roulette.stochastic_selection
ga.crossover_population_impl = EasyGA.Crossover_Methods.Population.sequential_selection
ga.crossover_individual_impl = EasyGA.Crossover_Methods.Individual.Arithmetic.int_random
ga.survivor_selection_impl   = EasyGA.Survivor_Selection.fill_in_best

ga.evolve()
ga.set_all_fitness()
ga.population.sort_by_best_fitness(ga)

print(f"Current Generation: {ga.current_generation}")
ga.population.print_all()
