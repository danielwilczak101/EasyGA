from copy import deepcopy

class Chromosome:

    def __init__(self, gene_list):
        """Initialize the chromosome with fitness value of None, and a
        set of genes dependent on user-passed parameter."""

        self.gene_list = [deepcopy(gene) for gene in gene_list]
        self.fitness = None


    def add_gene(self, gene, index = None):
        """Add a gene to the chromosome at the specified index, defaulted to end of the chromosome"""
        if index is None:
            index = len(self)
        self.gene_list.insert(index, gene)


    def remove_gene(self, index):
        """Removes the gene at the given index"""
        return self.gene_list.pop(index)


    @property
    def gene_value_list(self):
        """Returns a list of gene values"""
        return [gene.value for gene in self]


    @property
    def gene_value_iter(self):
        """Returns an iterable of gene values"""
        return (gene.value for gene in self)


    def __iter__(self):
        """
        Allows the user to use

                iter(chromosome)
                list(chromosome) == chromosome.gene_list
                tuple(chromosome)
                for gene in chromosome

        to loop through the chromosome.

        Note: using list(chromosome) creates a copy of
              the gene_list. Altering this will not
              alter the original gene_list.
        """
        return iter(self.gene_list)


    def __getitem__(self, index):
        """
        Allows the user to use
                gene = chromosome[index]
        to get the indexed gene.
        """
        return self.gene_list[index]


    def __setitem__(self, index, gene):
        """
        Allows the user to use
                chromosome[index] = gene
        to set the indexed gene.
        """
        self.gene_list[index] = gene


    def __len__(self):
        """
        Allows the user to use
                size = len(chromosome)
        to get the length of the chromosome.
        """
        return len(self.gene_list)


    def __contains__(self, searched_gene):
        """
        Allows the user to use
                if gene in chromosome
        to check if a gene is in the chromosome.
        """
        return (searched_gene in self.gene_list)


    def index_of(self, searched_gene):
        """
        Allows the user to use
                index = chromosome.index_of(gene)
        to find the index of a gene in the chromosome.
        Be sure to check if the chromosome contains the gene
        first, or to catch an exception if the gene is not
        in the chromosome.
        """
        return self.gene_list.index(searched_gene)


    def __eq__(self, chromosome):
        """
        Allows the user to use
                chromosome_1 == chromosome_2
                chromosome_1 != chromosome_2
        to compare two chromosomes based on their genes.
        """

        return all(gene_1 == gene_2 for gene_1, gene_2 in zip(self, chromosome))


    def __repr__(self):
        """
        Allows the user to use
                repr(chromosome)
        to get a backend representation of the chromosome.
        """
        return ', '.join(repr(gene) for gene in self)


    def __str__(self):
        """
        Allows the user to use
                str(chromosome)
                print(chromosome)
        to get a frontend representation of the chromosome.
        """
        return ''.join(str(gene) for gene in self)
