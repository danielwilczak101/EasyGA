import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

# input domain
#ga.domain = range(3, 10)
ga.domain = ['left', 'right']

# initialize random population
ga.initialize()

# Print population
ga.population.print_all()
