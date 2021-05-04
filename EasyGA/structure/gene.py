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
        """Comparing two genes by their value."""
        return self.value == Gene(other_gene).value


    def __hash__(self):
        """Hash genes by value so that they can be used in sets/dictionaries."""
        return hash(self.value)


    def __repr__(self):
        """
        Allows the user to use
                gene_string = repr(gene)
                gene_data   = eval(gene_string)
                gene        = ga.make_gene(gene_data)
        to get a backend representation of the gene.
        """
        return repr(self.value)


    def __str__(self):
        """
        Allows the user to use
                str(gene)
                print(gene)
        to get a frontend representation of the gene.
        """
        return f'[{str(self.value)}]'
