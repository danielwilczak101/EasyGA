class Termination_Methods:
    """Example functions that can be used to terminate the the algorithms loop"""

    def fitness_generation_tolerance(ga):
        """Terminate GA when any of the
        - fitness,
        - generation, or
        - tolerance
        goals are met."""

        # Need to start the algorithm if the population is None.
        if ga.population == None:
            return True

        # If fitness goal is set, check it.
        if ga.fitness_goal is not None:

            # If minimum fitness goal reached, stop ga.
            if ga.target_fitness_type == 'min' and ga.population.get_chromosome(0).get_fitness() <= ga.fitness_goal:
                return False

            # If maximum fitness goal reached, stop ga.
            elif ga.target_fitness_type == 'max' and ga.population.get_chromosome(0).get_fitness() >= ga.fitness_goal:
                return False

        # If generation goal is set, check it.
        if ga.generation_goal is not None and ga.current_generation >= ga.generation_goal:
            return False

        # If tolerance is set, check it.
        if ga.tolerance_goal is not None:

            best_fitness = ga.population.get_chromosome(0).get_fitness()
            threshhold_fitness = ga.population.get_chromosome(int(ga.percent_converged*ga.population.size())).get_fitness()
            tol = ga.tolerance_goal * (1 + abs(best_fitness))

            # Terminate if the specified amount of the population has converged to the specified tolerance
            if abs(best_fitness - threshhold_fitness) < tol:
                return False

        return True
