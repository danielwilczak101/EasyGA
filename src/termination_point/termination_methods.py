def _add_by_fitness_goal(termination_impl):
    """Adds termination by fitness goal to the method."""

    def new_method(ga):

        # If fitness goal is set, check it.
        if ga.fitness_goal is not None and ga.population is not None:

            # If minimum fitness goal reached, stop ga.
            if ga.target_fitness_type == 'min' and ga.population[0].fitness <= ga.fitness_goal:
                return False

            # If maximum fitness goal reached, stop ga.
            elif ga.target_fitness_type == 'max' and ga.population[0].fitness >= ga.fitness_goal:
                return False

        # Check other termination methods
        return termination_impl(ga)

    return new_method


def _add_by_generation_goal(termination_impl):
    """Adds termination by generation goal to the method."""

    def new_method(ga):

        # If generation goal is set, check it.
        if ga.generation_goal is not None and ga.current_generation >= ga.generation_goal:
            return False

        # Check other termination methods
        return termination_impl(ga)

    return new_method


def _add_by_tolerance_goal(termination_impl):
    """Adds termination by tolerance goal to the method."""

    def new_method(ga):

        # If tolerance is set, check it.
        if ga.tolerance_goal is not None and ga.population is not None:
            best_fitness = ga.population[0].fitness
            threshhold_fitness = ga.population[round(ga.percent_converged*len(ga.population))].fitness
            tol = ga.tolerance_goal * (1 + abs(best_fitness))

            # Terminate if the specified amount of the population has converged to the specified tolerance
            if abs(best_fitness - threshhold_fitness) < tol:
                return False

        # Check other termination methods
        return termination_impl(ga)

    return new_method


class Termination_Methods:
    """Example functions that can be used to terminate the the algorithms loop"""

    # Allowing access to decorators when importing class
    _add_by_fitness_goal    = _add_by_fitness_goal
    _add_by_generation_goal = _add_by_generation_goal
    _add_by_tolerance_goal  = _add_by_tolerance_goal


    @_add_by_fitness_goal
    @_add_by_generation_goal
    @_add_by_tolerance_goal
    def fitness_generation_tolerance(ga):
        """Terminate GA when any of the
        - fitness,
        - generation, or
        - tolerance
        goals are met."""

        return True
