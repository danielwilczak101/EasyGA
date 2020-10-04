import EasyGA
<<<<<<< Updated upstream
=======
import random

>>>>>>> Stashed changes

# Create the Genetic algorithm
ga = EasyGA.GA()

<<<<<<< Updated upstream
#Creating a gene with no fitness
gene1 = ga.make_gene("Im a gene")
gene2 = ga.make_gene("Im also a gene")
#Creating a Chromosome with no genes
chromosome = ga.make_chromosome()
chromosome.add_gene(gene1)
chromosome.add_gene(gene2)
# Creating a populaiton
populaiton = ga.make_population()
populaiton.add_chromosome(chromosome)

print(gene1)
print(chromosome)
print(populaiton)
populaiton.print_all()
=======
ga.gene_impl = [random.randrange,1,10]

# Run Everyhting
ga.evolve()

# Print the current population
ga.population.print_all()
>>>>>>> Stashed changes
