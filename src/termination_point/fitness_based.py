def fitness_based(ga):
    status = True
    if(ga.current_fitness > ga.goal_fitness):
        status = False
    return status
