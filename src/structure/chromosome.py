from copy import deepcopy

class Chromosome:

    def __init__(self, gene_list = []):
        """Initialize the chromosome with fitness value of None, and a
        set of genes dependent on user-passed parameter."""

        self.gene_list = deepcopy(gene_list)
        self.fitness = None


    def size(self):
        """Returns the number of genes in the chromosome"""
        return len(self.gene_list)


    def add_gene(self, gene, index = None):
        """Add a gene to the chromosome at the specified index, defaulted to end of the chromosome"""
        if index is None:
            index = self.size()
        self.gene_list.insert(index, gene)


    def remove_gene(self, index):
        """Removes the gene at the given index"""
        del self.gene_list[index]


    def get_gene(self, index):
        """Returns the gene at the given index"""
        return self.gene_list[index]


    def get_gene_list(self):
        return self.gene_list


    def get_fitness(self):
        """Return the fitness of the chromosome"""
        return self.fitness


    def set_gene(self, gene, index):
        self.gene_list[index] = gene


    def set_gene_list(self, genes):
        self.gene_list = genes


    def set_fitness(self, fitness):
        """Set the fitness value of the chromosome"""
        self.fitness = fitness


    def __repr__(self):
        """Create a backend string of the chromosome. Ex '1, 2, 3'."""
        return ', '.join(repr(gene) for gene in self.gene_list)


    def __str__(self):
        """Create a printable string of the chromosome. Ex '[1][2][3]'."""
        return ''.join(str(gene) for gene in self.gene_list)
