import EasyGA
import random

# Create the Genetic algorithm
ga = EasyGA.GA()
test_range_two = [["left", "right"],[22,88],5,[22,"up"]]
ga.initialize(test_range_two)
ga.population.print_all()




#test_range_one = [1,100]
#test_domain_one = ["left", "right", "up", "down"]
#test_range_two = [[1,100],[0,1],[33,35],[5,6]]
#test_domain_two = [["left", "right"], ["up", "down"], ["left", "down"], ["down", "right"]]

#for index-specific bounds, do list of lists i.e. test_range = [[1, 100], [1, 25], [5, 25]]