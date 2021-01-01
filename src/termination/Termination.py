# Import all termination decorators
from decorators import _add_by_fitness_goal, _add_by_generation_goal, _add_by_tolerance_goal

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
