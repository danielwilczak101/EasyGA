class Initialization_Methods:
    """Initialization examples that are used as defaults and examples"""

    def random_initialization(ga):
        """Takes the initialization inputs and
        - return a new population
          - filled with chromosomes
            - filled with genes
        """

        # Using the chromosome_impl to set every index inside of the chromosome
        if ga.chromosome_impl != None:
            return ga.make_population([
                       ga.make_chromosome([
                           ga.make_gene(ga.chromosome_impl(j))
                       for j in range(ga.chromosome_length)])
                   for i in range(ga.population_size)])

        # Using the gene_impl to set every gene to be the same
        elif ga.gene_impl != None:
            function = ga.gene_impl[0]
            return ga.make_population([
                       ga.make_chromosome([
                           ga.make_gene(function(*ga.gene_impl[1:]))
                       for j in range(ga.chromosome_length)])
                   for i in range(ga.population_size)])

        # Exit because no gene creation method specified
        else:
            print("You did not specify any initialization constraints.")
            return None
