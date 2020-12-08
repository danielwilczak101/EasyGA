import random

def _append_to_next_population(population_method):
    """Appends the new chromosomes to the next population.
    Also modifies the input to include the mating pool.
    """

    return lambda ga:\
        ga.population.append_children(
            population_method(ga, ga.population.mating_pool)
        )


def _check_weight(individual_method):
    """Checks if the weight is between 0 and 1 before running.
    Exception may occur when using ga.adapt, which will catch
    the error and try again with valid weight.
    """

    def new_method(ga, parent_1, parent_2, weight):

        if 0 < weight < 1:
            return individual_method(ga, parent_1, parent_2, weight)
        else:
            raise ValueError("""Weight must be between 0 and 1 when using
             the given crossover method.""")

    return new_method


def _genes_to_chromosome(individual_method):
    """Converts a collection of genes into a chromosome.
    Note: Will recreate the gene list if given gene list.
          Built-in methods do not construct gene lists
          and use yield for efficiency.
    """

    return lambda ga, parent_1, parent_2, weight:\
        ga.make_chromosome(
            individual_method(ga, parent_1, parent_2, weight)
        )


def _values_to_genes(individual_method):
    """Converts a collection of values into genes.
    Returns a generator of genes to avoid storing a new list.
    """

    return lambda ga, parent_1, parent_2, weight:\
        (
            ga.make_gene(value)
            for value
            in individual_method(ga, parent_1, parent_2, weight)
        )


class Crossover_Methods:

    # Allowing access to decorators when importing class
    _append_to_next_population = _append_to_next_population
    _check_weight              = _check_weight
    _genes_to_chromosome       = _genes_to_chromosome
    _values_to_genes           = _values_to_genes


    class Population:
        """Methods for selecting chromosomes to crossover."""


        @_append_to_next_population
        def sequential_selection(ga, mating_pool):
            """Select sequential pairs from the mating pool.
            Every parent is paired with the previous parent.
            The first parent is paired with the last parent.
            """

            for index in range(len(mating_pool)):    # for each parent in the mating pool
                yield ga.crossover_individual_impl(  #     apply crossover to
                    ga,                              #
                    mating_pool[index],              #         the parent and
                    mating_pool[index-1],            #         the previous parent
                    0.5                              #         with equal weight
                )


        @_append_to_next_population
        def random_selection(ga, mating_pool):
            """Select random pairs from the mating pool.
            Every parent is paired with a random parent.
            """

            for parent in mating_pool:               # for each parent in the mating pool
                yield ga.crossover_individual_impl(  #     apply crossover to
                    ga,                              #
                    parent,                          #         the parent and
                    random.choice(mating_pool),      #         a random parent
                    0.5                              #         with equal weight
                )


    class Individual:
        """Methods for crossing parents."""


        @_check_weight
        @_genes_to_chromosome
        def single_point(ga, parent_1, parent_2, weight = 0.5):
            """Cross two parents by swapping genes at one random point."""

            minimum_parent_length = min(len(parent_1), len(parent_2))

            # Equally weighted indexes
            if weight == 0.5:
                swap_index = random.randrange(minimum_parent_length)

            # Use weighted random index.
            else:
                weight_conversion = 2*weight if (weight < 0.5) else 0.5 / (1-weight)
                rand_num = random.random()
                swap_index = int(
                    minimum_parent_length *
                        (1-(1-rand_num)**weight_conversion)**(1/weight_conversion)
                    )

            # Randomly choose which parent's genes are selected first.
            if random.choice([True, False]):
                return parent_1[:swap_index] + parent_2[swap_index:]
            else:
                return parent_2[:-swap_index] + parent_1[-swap_index:]


        @_check_weight
        @_genes_to_chromosome
        def multi_point(ga, parent_1, parent_2, weight = 0.5):
            """Cross two parents by swapping genes at multiple points."""
            pass


        @_check_weight
        @_genes_to_chromosome
        def uniform(ga, parent_1, parent_2, weight = 0.5):
            """Cross two parents by swapping all genes randomly."""

            for gene_pair in zip(parent_1, parent_2):
                yield random.choices(gene_pair, cum_weights = [weight, 1])[0]


        class Arithmetic:
            """Crossover methods for numerical genes."""

            @_genes_to_chromosome
            @_values_to_genes
            def average(ga, parent_1, parent_2, weight = 0.5):
                """Cross two parents by taking the average of the genes."""

                values_1 = parent_1.gene_value_iter
                values_2 = parent_2.gene_value_iter

                for value_1, value_2 in zip(values_1, values_2):

                    value = weight*value_1 + (1-weight)*value_2

                    if type(value_1) == type(value_2) == int:
                        value = round(value + random.uniform(-0.5, 0.5))

                    yield value


            @_genes_to_chromosome
            @_values_to_genes
            def extrapolate(ga, parent_1, parent_2, weight = 0.5):

                """Cross two parents by extrapolating towards the first parent.
                May result in gene values outside the expected domain.
                """

                values_1 = parent_1.gene_value_iter
                values_2 = parent_2.gene_value_iter

                for value_1, value_2 in zip(values_1, values_2):

                    value = (2-weight)*value_1 + (weight-1)*value_2

                    if type(value_1) == type(value_2) == int:
                        value = round(value + random.uniform(-0.5, 0.5))

                    yield value


            @_check_weight
            @_genes_to_chromosome
            @_values_to_genes
            def random(ga, parent_1, parent_2, weight = 0.5):
                """Cross two parents by taking a random integer or float value between each of the genes."""

                values_1 = parent_1.gene_value_iter
                values_2 = parent_2.gene_value_iter

                for value_1, value_2 in zip(values_1, values_2):

                    # Use equally weighted values.
                    if weight == 0.5:
                        value = random.uniform(value_1, value_2)

                    # Use weighted random value, which gives values closer
                    # to value_1 if weight < 0.5 or values closer to value_2
                    # if weight > 0.5.
                    else:
                        t = 2*weight if (weight < 0.5) else 0.5 / (1-weight)
                        x = random.random()
                        value = value_1 + (value_2-value_1) * (1-(1-x)**t)**(1/t)

                    if type(value_1) == type(value_2) == int:
                        value = round(value + random.uniform(-0.5, 0.5))

                    yield value

        class Permutation:
            """Crossover methods for permutation based chromosomes."""

            @_check_weight
            @_genes_to_chromosome
            def ox1(ga, parent_1, parent_2, weight = 0.5):
                """Cross two parents by slicing out a random part of one parent
                and then filling in the rest of the genes from the second parent."""

                # Swap with weighted probability so that most of the genes
                # are taken directly from parent 1.
                if random.choices([0, 1], cum_weights = [weight, 1]) == 1:
                    parent_1, parent_2 = parent_2, parent_1

                # Extract genes from parent 1 between two random indexes
                index_2 = random.randrange(1, len(parent_1))
                index_1 = random.randrange(index_2)

                # Create copies of the gene lists
                gene_list_1 = [None]*index_1 + parent_1[index_1:index_2] + [None]*(len(parent_1)-index_2)
                gene_list_2 = list(parent_2)

                input_index = 0

                # For each gene from the second parent
                for _ in range(len(gene_list_2)):

                    # Remove it if it is already used
                    if gene_list_2[-1] in gene_list_1:
                        gene_list_2.pop(-1)

                    # Add it if it has not been used
                    else:
                        if input_index == index_1:
                            input_index = index_2
                        gene_list_1[input_index] = gene_list_2.pop(-1)
                        input_index += 1

                return gene_list_1


            @_check_weight
            @_genes_to_chromosome
            def partially_mapped(ga, parent_1, parent_2, weight = 0.5):
                """Cross two parents by slicing out a random part of one parent
                and then filling in the rest of the genes from the second parent,
                preserving the ordering of genes wherever possible."""

                # Swap with weighted probability so that most of the genes
                # are taken directly from parent 1.
                if random.choices([0, 1], cum_weights = [weight, 1]) == 1:
                    parent_1, parent_2 = parent_2, parent_1

                # Extract genes from parent 1 between two random indexes
                index_2 = random.randrange(1, len(parent_1))
                index_1 = random.randrange(index_2)

                # Create copies of the gene lists
                gene_list_1 = [None]*index_1 + parent_1[index_1:index_2] + [None]*(len(parent_1)-index_2)
                gene_list_2 = list(parent_2)

                # Create hash for gene list 2
                hash = {gene:index for index, gene in enumerate(gene_list_2)}

                # For each gene in the copied segment from parent 2
                for i in range(index_1, index_2):

                    # If it is not already copied,
                    # find where it got displaced to
                    j = i
                    while gene_list_1[(j := hash[gene_list_1[j]])] is not None:
                        pass
                    gene_list_1[j] = gene_list_2[i]

                # Fill in whatever is leftover (copied from ox1).
                # For each gene from the second parent
                for _ in range(len(gene_list_2)):

                    # Remove it if it is already used
                    if gene_list_2[-1] in gene_list_1:
                        gene_list_2.pop(-1)

                    # Add it if it has not been used
                    else:
                        if input_index == index_1:
                            input_index = index_2
                        gene_list_1[input_index] = gene_list_2.pop(-1)
                        input_index += 1

                return gene_list_1
