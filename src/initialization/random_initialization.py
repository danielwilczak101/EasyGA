# Import the data structure
from .population_structure.population import population as create_population
from .chromosome_structure.chromosome import chromosome as create_chromosome
from .gene_structure.gene import gene as create_gene

def random_initialization(population_size, chromosome_length, chromosome_impl, gene_impl):
    """Takes the initialization inputs and choregraphs them to output the type of population
    with the given parameters."""
    # Create the population object
    population = create_population()
    
    # Fill the population with chromosomes
    for i in range(population_size):
        chromosome = create_chromosome()
        #Fill the Chromosome with genes
        for j in range(chromosome_length):
            # Using the chromosome_impl to set every index inside of the chromosome
            if chromosome_impl != None:
                # Each chromosome location is specified with its own function
                chromosome.add_gene(create_gene(chromosome_impl(j)))
                # Will break if chromosome_length != len(lists) in domain
            elif gene_impl != None:
                # gene_impl = [range function,lowerbound,upperbound]
                function = gene_impl[0]
                chromosome.add_gene(create_gene(function(*gene_impl[1:])))
            else:
                #Exit because either were not specified
                print("Your domain or range were not specified")
        population.add_chromosome(chromosome)
    return population
