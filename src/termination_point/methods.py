class Termination_methods:
    """Example functions that can be used to terminate the the algorithms loop"""

    def fitness_based(ga):
        """Fitness based approach to terminate when the goal fitness has been reached"""
        status = True
        if(ga.current_fitness > ga.fitness_goal):
            status = False
        return status

    def generation_based(ga):
        """Generation based approach to terminate when the goal generation has been reached"""
        status = True
        if(ga.current_generation > ga.generation_goal):
            status = False
        return status
