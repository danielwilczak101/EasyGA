import EasyGA
import random

#1. GA should take in range for gene input
#2. GA should take in index-dependent range for gene input
#3. GA should take in domain input
#4. GA should take in index-dependent domain for gene input
#5. GA should accept mix of range and domain for gene input


# Create the Genetic algorithm
ga = EasyGA.GA()
test_gene_input = [["left", "right"],[1,100],[5.0,10],[22,"up"]]
#ga.gene_input_type[1] = "domain"
#ga.gene_input_type[1] = "float-range"
ga.initialize(test_gene_input)
ga.population.print_all() 




#test_range_one = [1,100]
#test_domain_one = ["left", "right", "up", "down"]
#test_range_two = [[1,100],[0,1],[33,35],[5,6]]
#test_domain_two = [["left", "right"], ["up", "down"], ["left", "down"], ["down", "right"]]

#for index-specific bounds, do list of lists i.e. test_range = [[1, 100], [1, 25], [5, 25]]