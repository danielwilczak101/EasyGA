class Fitness_Examples:
    """Fitness function examples used"""
    def is_it_5(self, chromosome):
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

    def index_dependent_values(self, chromosome):
        """A very simple case test function - If the chromosomes gene value is a 5 add one
         to the chromosomes overall fitness value."""
        # Overall fitness value
        fitness = 0
        # For each gene in the chromosome
        for i in range(len(chromosome.gene_list)):
            if (chromosome.gene_list[i].value == i+1):
                fitness += 1
                
        return fitness
