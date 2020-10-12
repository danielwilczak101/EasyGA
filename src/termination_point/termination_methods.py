class Termination_Methods:
    """Example functions that can be used to terminate the the algorithms loop"""

    def fitness_based(ga):
        """Fitness based approach to terminate when the goal fitness has been reached"""
        
        if ga.population == None:
            return True
        for i in range(ga.population.size()):
            if(ga.population.get_all_chromosomes()[i].fitness >= ga.fitness_goal):
                return False
        return True

    def generation_based(ga):
        """Generation based approach to terminate when the goal generation has been reached"""
        
        return ga.current_generation < ga.generation_goal
