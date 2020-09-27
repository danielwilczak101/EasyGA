import EasyGA
import random
# Create the Genetic algorithm
ga = EasyGA.GA()

def user_gene_domain(gene_index):
    """Each gene index is assosiated to its index in the chromosome"""
    chromosome = [
    random.randrange(1,100),
    random.uniform(10,5),
    random.choice(["up","down"])
    ]
    return chromosome[gene_index]

# If the user wants to use a domain
ga.chromosome_impl = user_gene_domain

ga.initialize_population()

ga.population.print_all()
