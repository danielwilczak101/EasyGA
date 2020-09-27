# Import the data structure
from .population_structure.population import population as create_population
from .chromosome_structure.chromosome import chromosome as create_chromosome
from .gene_structure.gene import gene as create_gene

def random_initialization(population_size, chromosome_length, domain, new_range):
    # Create the population object
    population = create_population()
    # Fill the population with chromosomes
    for i in range(population_size):
        chromosome = create_chromosome()
        #Fill the Chromosome with genes
        for j in range(chromosome_length):
            if domain != None:
                # Each chromosome location is specified with its own function
                chromosome.add_gene(create_gene(domain(j)))
                # Will break if chromosome_length != lists in domain
            elif new_range != None:
                # new_rnage = [range function,lowerbound,upperbound]
                function = new_range[0]
                chromosome.add_gene(create_gene(function(new_range[1],new_range[2])))
            else:
                #Exit because either were not specified
                print("Your domain or range were not specified")
        population.add_chromosome(chromosome)
    return population
