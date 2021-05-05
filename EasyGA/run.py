import EasyGA
import random

# Create the Genetic algorithm
ga = EasyGA.GA()

ga.save_data = False

def is_it_5(chromosome):
        """A very simple case test function - If the chromosomes gene value is a 5 add one
         to the chromosomes overall fitness value."""
        # Overall fitness value
        fitness = 0
        # For each gene in the chromosome
        for gene in chromosome.gene_list:
            # Check if its value = 5
            if(gene.value == 5):
                # If its value is 5 then add one to
                # the overal fitness of the chromosome.
                fitness += 1

        return fitness

ga.fitness_function_impl = is_it_5

# Create random genes from 0 to 10
ga.gene_impl = lambda: random.randint(0, 10)

ga.evolve()

# Print your default genetic algorithm
ga.print_generation()
ga.print_population()
