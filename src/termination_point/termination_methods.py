class Termination_Methods:
    """Example functions that can be used to terminate the the algorithms loop"""

    def fitness_and_generation_based(ga):
        """Fitness based approach to terminate when the goal fitness has been reached"""

        # Need to start the algorithm if the population is None.
        if ga.population == None:
            return True

        # If minimum fitness goal reached, stop ga.
        if ga.target_fitness_type == 'min' and ga.get_chromosome_fitness(0) >= ga.convert_fitness(ga.fitness_goal):
            return False

        # If maximum fitness goal reached, stop ga.
        if ga.target_fitness_type == 'max' and ga.get_chromosome_fitness(0) >= ga.convert_fitness(ga.fitness_goal):
            return False
        
        # Otherwise continue ga.
        return ga.current_generation < ga.generation_goal
