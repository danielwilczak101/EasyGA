def is_the_value_5(chromosome):
    """A very simple case test function - If the chromosomes gene value is a 5 add one
     to the chromosomes overall fitness value."""

    # Overall fitness value
    fitness = 0
    # For each gene in the chromosome
    for gene in chromosome.genes:
        # Check if its value = 5
        if(gene.value == 5):
            # If its value is 5 then add one to
            # the overal fitness of the chromosome.
            fitness += 1
    return fitness
