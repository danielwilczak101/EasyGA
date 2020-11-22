class Fitness_Examples:
    """Fitness function examples used"""

    def is_it_5(chromosome):
        """A very simple case test function - If the chromosomes gene value is a 5 add one
         to the chromosomes overall fitness value."""
        # Overall fitness value
        fitness = 0
        # For each gene in the chromosome
        for gene in chromosome:
            # Check if its value = 5
            if(gene.value == 5):
                # If its value is 5 then add one to
                # the overal fitness of the chromosome.
                fitness += 1
                
        return fitness


    def near_5(chromosome):
        """Test's the GA's ability to handle floats.
        Computes how close each gene is to 5.
        """
        return sum([1-pow(1-gene.value/5, 2) for gene in chromosome])


    def index_dependent_values(chromosome):
        """Test of the GA's ability to improve fitness when the value is index-dependent.
        If a gene is equal to its index in the chromosome + 1, fitness is incremented.
        """
        fitness = 0
        for i in range(len(chromosome)):
            if (chromosome[i].value == i+1):
                fitness += 1
                
        return fitness
