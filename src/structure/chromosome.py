from copy import deepcopy

class Chromosome:

    def __init__(self, gene_list = []):
        """Initialize the chromosome with fitness value of None, and a
        set of genes dependent on user-passed parameter."""

        self.gene_list = deepcopy(gene_list)
        self.fitness = None


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


    def set_gene_list(self, gene_list):
        self.gene_list = gene_list


    def set_fitness(self, fitness):
        """Set the fitness value of the chromosome"""
        self.fitness = fitness


    @property
    def gene_value_list(self):
        """Returns a list of gene values"""
        return [gene.value for gene in self]


    def __iter__(self):
        """Returns an iterable of the gene list"""
        return iter(self.gene_list)


    def __getitem__(self, k):
        """Returns the k-th gene"""
        return self.get_gene(k)


    def __setitem__(self, k, gene):
        """Sets the k-th gene value"""
        self.set_gene(gene, k)


    def __len__(self):
        """Returns the number of genes in the chromosome"""
        return len(self.gene_list)


    def __repr__(self):
        """Create a backend string of the chromosome. Ex '1, 2, 3'."""
        return ', '.join(repr(gene) for gene in self.gene_list)


    def __str__(self):
        """Create a printable string of the chromosome. Ex '[1][2][3]'."""
        return ''.join(str(gene) for gene in self.gene_list)
