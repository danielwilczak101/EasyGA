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
ga.gene_input_type[1] = "float-range"
ga.gene_input_type[2] = "domain"

ga.initialize(test_gene_input)
ga.population.print_all() 


#Example tests
#Note, the following examples assume a chromosome length of 4.
#if the test_gene_input is longer than the chromosomes, it will get truncated at the length of the chromosome
#for example, for chromosomes with length 2, [["left", "right"],[1,100],[5.0,10],[22,"up"]] becomes [["left", "right"],[1,100]]
#if the test_gene_input is shorter than the chromosomes, the remaining elements will be populated with None

#test_gene_input = [1,100]
#test_gene_input = [["left", "right"],[1,100],[5.0,10],[22,"up"]]
#test_gene_input = ["left", "right", "up", "down"]
#test_gene_input = [[1,100],[0,1],[33,35],[5,6]]
#test_gene_input = [["left", "right"], ["up", "down"], ["left", "down"], ["down", "right"]]

#ga.gene_input_type = "float-range"
#ga.gene_input_type[1] = "domain"
#ga.gene_input_type[1] = "float-range"