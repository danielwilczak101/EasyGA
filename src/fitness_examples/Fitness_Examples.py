def is_it_5(self, chromosome):
    """A very simple case test function - If the chromosome's gene value
    is equal to 5 add one to the chromosomes overall fitness value.
    """

    # Overall fitness value
    fitness = 0

    for gene in chromosome:

        # Increment fitness is the gene's value is 5
        if gene.value == 5:
            fitness += 1

    return fitness


def near_5(self, chromosome):
    """Test's the GA's ability to handle floats. Computes how close each gene is to 5."""

    # Overall fitness value
    fitness = 0

    for gene in chromosome:

        # Add squared distance to 5
        fitness += (5 - gene.value) ** 2

    return fitness


def index_dependent_values(self, chromosome):
    """Test of the GA's ability to improve fitness when the value is index-dependent.
    If a gene is equal to its index in the chromosome + 1, fitness is incremented.
    """

    # Overall fitness value
    fitness = 0

    for i, gene in enumerate(chromosome):

        # Increment fitness is the gene's value is i+1
        if gene.value == i+1:
            fitness += 1

    return fitness
