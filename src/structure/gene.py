from copy import deepcopy

class Gene:

    def __init__(self, value):
        """Initialize a gene with the input value."""

        # Copy another gene
        try:
            self.value = deepcopy(value.value)

        # Otherwise copy the given value
        except:
            self.value = deepcopy(value)


    def __eq__(self, other_gene):
        """Comparing two genes by their value.
        Returns False if either gene is None."""

        if (self is None) or (other_gene is None):
            return False
        else:
            return self.value == other_gene.value


    def __repr__(self):
        """
        Allows the user to use
                gene_string = repr(gene)
                gene = eval(gene_string)
        to get a backend representation of the gene.
        """
        return f"EasyGA.make_gene({repr(self.value)})"


    def __str__(self):
        """
        Allows the user to use
                str(gene)
                print(gene)
        to get a frontend representation of the gene.
        """
        return f'[{str(self.value)}]'
