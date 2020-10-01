class selection_examples:
    """Selection defintion here"""

    """Tournament selection involves running several "tournaments" among a
    few individuals (or "chromosomes")chosen at random from the population.
    The winner of each tournament (the one with the best fitness) is selected
    for crossover.

    Ex
    Chromsome 1----1 wins ------
    Chromsome 2----            - --1 wins----
                               -            -
    Chromsome 3----3 wins ------            -- 5 Wins --->Chromosome 5 becomes Parent
    Chromsome 4----                         -
                                            -
    Chromsome 5----5 wins ---------5 wins----
    Chromsome 6----
   ^--Matchs--^
    """

    def match_based_tournament(ga, matchs):
        # User selects how many matchs they want to start with to create one parent.

        # Select two random parents
        selected_1_index = random.randint(0, len(ga.population.chromosomes) - 1)]
        selected_2_index = random.randint(0, len(ga.population.chromosomes) - 1)]

        if selected_1_index <= selected_2_index:
            return parent1
        else:
            return parent2

    def small_tournament(ga):
        """ Small tournament is only one round of tournament. Beat the other
        randomly selected chromosome and your are selected as a parent.

        Chromosome 1----
                        - 1 wins -> Becomes selected for crossover.
        Chromosome 2----            -
        """
        # Select two random parents

        selected_1_index = random.randint(0, len(ga.population.chromosomes) - 1)]
        selected_2_index = random.randint(0, len(ga.population.chromosomes) - 1)]

        if selected_1 <= fitness2:
            return parent1
        else:
            return parent2

    def population_based_tournament(ga):
        """The size of the population dictates how many matchs there will be. The
        greater the size of the population the more matchs there is."""
        pass

    def roulette(ga):
        """Roulette selection works based off of how strong the fitness is of the
        chromosomes in the population. The stronger the fitness the higher the probability
        that it will be selected. Using the example of a casino roulette wheel.
        Where the chromosomes are the numbers to be selected and the board size for
        those numbers are directly proportional to the chromosome's current fitness. Where
        the ball falls is a randomly generated number between 0 and 1"""
        pass
