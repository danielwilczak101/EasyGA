import random

def append_to_next_population(population_method):
    """Appends the new chromosomes to the next population.
    Also modifies the input to include the mating pool.
    """

    return lambda ga:\
        ga.population.append_children(
            list(population_method(ga, ga.population.mating_pool))
        )


def weak_check_exceptions(population_method):
    """Checks if the first and last chromosomes can be crossed."""

    def new_method(ga, mating_pool):

        # check if any genes are an Exception from
        # crossing just the first and last parents.
        for gene in ga.crossover_individual_impl(ga, mating_pool[0], mating_pool[-1]):
            if isinstance(gene.value, Exception):
                raise gene.value

        # continue if no Exceptions found.
        else:
            return population_method(ga, ga.population.mating_pool)

    return new_method


def strong_check_exceptions(population_method):
    """Checks if every pair of selected chromosomes can be crossed.
    Warning: Very slow, consider comparing the types of genes
             allowed to the method used beforehand instead.
    """

    def new_method(ga, mating_pool):

        next_population = list(population_method(ga, ga.population.mating_pool))

        # check if any genes are an Exception.
        for chromosome in next_population:
            for gene in chromosome:
                if isinstance(gene.value, Exception):
                    raise gene.value

        # continue if no Exceptions found.
        else:
            return next_population

    return new_method


def genes_to_chromosome(individual_method):
    """Converts a collection of genes into a chromosome.
    Note: Will recreate the gene list if given gene list.
          Built-in methods do not construct gene lists
          and use yield for efficiency.
    """

    return lambda ga, parent_1, parent_2:\
        ga.make_chromosome(
            list(individual_method(ga, parent_1, parent_2))
        )


def values_to_genes(individual_method):
    """Converts a collection of values into genes.
    Returns a generator of genes to avoid storing a new list.
    """

    return lambda ga, parent_1, parent_2:\
        (
            ga.make_gene(value)
            for value
            in individual_method(ga, parent_1, parent_2)
        )


class Crossover_Methods:

    # Private method decorators, see above.
    _append_to_next_population = append_to_next_population
    _weak_check_exceptions     = weak_check_exceptions
    _strong_check_exceptions   = strong_check_exceptions
    _genes_to_chromosome       = genes_to_chromosome
    _values_to_genes           = values_to_genes


    class Population:
        """Methods for selecting chromosomes to crossover."""


        @append_to_next_population
        @weak_check_exceptions
        def sequential_selection(ga, mating_pool):
            """Select sequential pairs from the mating pool.
            Every parent is paired with the previous parent.
            The first parent is paired with the last parent.
            """

            for index in range(len(mating_pool)):    # for each parent in the mating pool
                yield ga.crossover_individual_impl(  #     apply crossover to
                    ga,                              # 
                    mating_pool[index],              #         the parent and
                    mating_pool[index-1]             #         the previous parent
                )


        @append_to_next_population
        @weak_check_exceptions
        def random_selection(ga, mating_pool):
            """Select random pairs from the mating pool.
            Every parent is paired with a random parent.
            """

            for parent in mating_pool:               # for each parent in the mating pool
                yield ga.crossover_individual_impl(  #     apply crossover to
                    ga,                              # 
                    parent,                          #         the parent and
                    random.choice(mating_pool)       #         a random parent
                )


    class Individual:
        """Methods for crossing parents."""


        @genes_to_chromosome
        def single_point(ga, parent_1, parent_2):
            """Cross two parents by swapping genes at one random point."""

            swap_index = random.randrange(len(parent_1))
            return parent_1[:swap_index] + parent_2[swap_index:]


        @genes_to_chromosome
        def multi_point(ga, parent_1, parent_2):
            """Cross two parents by swapping genes at multiple points."""
            pass


        @genes_to_chromosome
        def uniform(ga, parent_1, parent_2):
            """Cross two parents by swapping all genes randomly."""

            for gene_pair in zip(parent_1, parent_2):
                yield random.choice(gene_pair)


        class Arithmetic:
            """Crossover methods for numerical genes."""

            @genes_to_chromosome
            @values_to_genes
            def random(ga, parent_1, parent_2):
                """Cross two parents by taking a random integer or float value between each of the genes."""

                value_iter_1 = parent_1.gene_value_iter
                value_iter_2 = parent_2.gene_value_iter

                for value_1, value_2 in zip(value_iter_1, value_iter_2):
                    if type(value_1) == type(value_2) == int:
                        yield random.randint(*sorted([value_1, value_2]))
                    else:
                        try:
                            yield random.uniform(value_1, value_2)
                        except:
                            yield ValueError("Unhandled gene type found. Use integer or float genes.")


            @genes_to_chromosome
            @values_to_genes
            def average(ga, parent_1, parent_2):
                """Cross two parents by taking a a weighted average of the genes."""

                value_iter_1 = parent_1.gene_value_iter
                value_iter_2 = parent_2.gene_value_iter

                for value_1, value_2 in zip(value_iter_1, value_iter_2):
                    if type(value_1) == type(value_2) == int:
                        yield (value_1+value_2)//2
                    else:
                        try:
                            yield (value_1+value_2)/2
                        except:
                            raise ValueError("Could not take the average of the gene values. Use integer or float genes.")
