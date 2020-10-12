class Termination_Methods:
    """Example functions that can be used to terminate the the algorithms loop"""

    def fitness_based(ga):
        """Fitness based approach to terminate when the goal fitness has been reached"""

        # Need to start the algorithm if the population is None
        if ga.population == None:
            return True

        # Check all chromosomes
        for chromosome in ga.population.get_all_chromosomes():

            # Stop if a chromosome has reached the fitness_goal
            if(chromosome.fitness >= ga.fitness_goal):
                return False

        # Continue if no chromosomes have reached the fitness goal
        return True


    def generation_based(ga):
        """Generation based approach to terminate when the goal generation has been reached"""

        return ga.current_generation < ga.generation_goal
