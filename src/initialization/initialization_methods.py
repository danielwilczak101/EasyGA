def _chromosomes_to_population(initialize):
    """Makes a population from chromosomes."""
    return lambda ga:\
        ga.make_population(
            [
                initialize(ga)
                for _
                in range(ga.population_size)
            ]
        )

def _genes_to_chromosome(initialize):
    """Converts a collection of genes to a chromosome."""
    return lambda ga:\
        ga.make_chromosome(
            list(initialize(ga))
        )

def _values_to_genes(initialize):
    """Converts a collection of values to genes."""
    return lambda ga:\
        (
            ga.make_gene(value)
            for value
            in initialize(ga)
        )


class Initialization_Methods:
    """Initialization examples that are used as defaults and examples"""

    # Private method decorators, see above.
    _chromosomes_to_population = _chromosomes_to_population
    _genes_to_chromosome       = _genes_to_chromosome
    _values_to_genes           = _values_to_genes


    @_chromosomes_to_population
    @_genes_to_chromosome
    @_values_to_genes
    def random_initialization(ga):
        """Takes the initialization inputs and returns a collection of values.
        Method decorators convert them to a GA population object.
        """

        # Using the chromosome_impl to set every index inside of the chromosome
        if ga.chromosome_impl is not None:
            for value in ga.chromosome_impl():
                yield value

        # Using the gene_impl to set every gene to be the same
        elif ga.gene_impl is not None:
            for _ in range(ga.chromosome_length):
                yield ga.gene_impl()

        # Exit because no gene creation method specified
        else:
            raise Exception("Did not specify any initialization constraints.")
