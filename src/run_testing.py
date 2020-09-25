import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

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
