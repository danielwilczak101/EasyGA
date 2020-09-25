import EasyGA
import random
# Create the Genetic algorithm
ga = EasyGA.GA()

def user_gene_domain(gene_index):
    """Each gene index is assosiated to its index in the chromosome"""
    domain = [
    random.randrange(1,100,5),
    random.uniform(10,5),
    random.choice(["up","down"])
    ]
    return domain[gene_index]

print(user_gene_domain(0))

# If the user wants to use a domain
ga.domain = user_gene_domain
# If the user wants to use a custom range
#ga.new_range = [random.randrange,1,100,None]

ga.initialize()

#ga.population.print_all()
