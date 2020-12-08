from copy import deepcopy

class Gene:

    def __init__(self, value):
        """Initialize a gene with fitness of value None and the input value."""
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
                repr(gene)
        to get a backend representation of the gene.
        """
        return str(self.value)


    def __str__(self):
        """
        Allows the user to use
                str(gene)
                print(gene)
        to get a frontend representation of the gene.
        """
        return f'[{str(self.value)}]'
