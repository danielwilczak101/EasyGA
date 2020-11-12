class Initialization_Methods:
    """Initialization examples that are used as defaults and examples"""

    def random_initialization(ga):
        """Takes the initialization inputs and
        - return a new population
          - filled with chromosomes
            - filled with genes
        """

        # Using the chromosome_impl to set every index inside of the chromosome
        if ga.chromosome_impl is not None:
            return ga.make_population([
                       ga.make_chromosome([
                           ga.make_gene(value)
                       for value in ga.chromosome_impl()])
                   for i in range(ga.population_size)])

        # Using the gene_impl to set every gene to be the same
        elif ga.gene_impl is not None:
            return ga.make_population([
                       ga.make_chromosome([
                           ga.make_gene(ga.gene_impl())
                       for j in range(ga.chromosome_length)])
                   for i in range(ga.population_size)])

        # Exit because no gene creation method specified
        else:
            print("You did not specify any initialization constraints.")
            return None
