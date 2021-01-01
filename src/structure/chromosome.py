from structure import Gene as make_gene
from itertools import chain

def to_gene(gene):
    """Converts the input to a gene if it isn't already one."""

    if isinstance(gene, make_gene):
        return gene
    else:
        return make_gene(gene)


class Chromosome():

    def __init__(self, gene_list):
        """Initialize the chromosome with fitness value of None, and a
        set of genes dependent on user-passed parameter."""

        self.gene_list = [make_gene(gene) for gene in gene_list]
        self.fitness = None


    @property
    def gene_value_list(self):
        """Returns a list of gene values"""
        return [gene.value for gene in self]


    @property
    def gene_value_iter(self):
        """Returns an iterable of gene values"""
        return (gene.value for gene in self)


    #==================================================#
    # Magic-Dunder Methods replicating list structure. #
    #==================================================#


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

        # Single gene
        if isinstance(index, int):
            self.gene_list[index] = to_gene(gene)

        # Multiple genes
        else:
            self.gene_list[index] = [to_gene(item) for item in gene]


    def __delitem__(self, index):
        """
        Allows the user to use
                del chromosome[index]
        to delete a gene at the specified index.
        """
        del self.gene_list[index]


    def __len__(self):
        """
        Allows the user to use
                size = len(chromosome)
        to get the length of the chromosome.
        """
        return len(self.gene_list)


    def __contains__(self, gene):
        """
        Allows the user to use
                if gene in chromosome
        to check if a gene is in the chromosome.
        """
        return (to_gene(gene) in self.gene_list)


    def __eq__(self, chromosome):
        """Returns self == chromosome, True if all genes match."""
        return self.gene_list == chromosome.gene_list


    def __add__(self, chromosome):
        """Return self + chromosome, a chromosome made by concatenating the genes."""
        return Chromosome(chain(self, chromosome))


    def __iadd__(self, chromosome):
        """Implement self += chromosome by concatenating the new genes."""
        self.gene_list += (to_gene(gene) for gene in chromosome)


    def append(self, gene):
        """Append gene to the end of the chromosome."""
        self.gene_list.append(to_gene(gene))


    def clear(self):
        """Remove all genes from chromosome."""
        self.gene_list = []


    def copy(self):
        """Return a copy of the chromosome."""
        return Chromosome(self)


    def count(self, gene):
        """Return number of occurrences of the gene in the chromosome."""
        return self.gene_list.count(to_gene(gene))


    def index(self, gene, guess = None):
        """
        Allows the user to use
                index = chromosome.index(gene)
                index = chromosome.index(gene, guess)
        to find the index of a gene in the chromosome.

        If no guess is given, it finds the index of the first match.
        If a guess is given, it finds index of the nearest match.
        """

        # Cast to gene object
        gene = to_gene(gene)

        # Use built-in method
        if guess is None:
            return self.gene_list.index(gene)

        # Use symmetric mod
        guess %= len(self)
        if guess >= len(self)//2:
            guess -= len(self)

        # Search outwards for the gene
        for i in range(1+len(self)//2):

            # Search to the left
            if gene == self[guess-i]:
                return (guess-i) % len(self)

            # Search to the right
            elif gene == self[guess+i]:
                return (guess+i) % len(self)

        # Gene not found
        raise ValueError("No such gene in the chromosome found")


    def insert(self, index, gene):
        """Insert gene so that self[index] == gene."""
        self.gene_list.insert(index, to_gene(gene))


    def pop(self, index = -1):
        """Remove and return gene at index (default last).

        Raises IndexError if chromosome is empty or index is out of range.
        """
        return self.gene_list.pop(index)


    def remove(self, gene):
        """Remove first occurrence of gene.

        Raises ValueError if the gene in not present.
        """
        self.gene_list.remove(to_gene(gene))


    def __repr__(self):
        """
        Allows the user to use
                chromosome_string = repr(chromosome)
                chromosome_data   = eval(chromosome_string)
                chromosome        = ga.make_chromosome(chromosome_data)
        to get a backend representation of the chromosome
        which can be evaluated directly as code to create
        the chromosome.
        """
        return repr(self.gene_list)


    def __str__(self):
        """
        Allows the user to use
                str(chromosome)
                print(chromosome)
        to get a frontend representation of the chromosome.
        """
        return ''.join(str(gene) for gene in self)
