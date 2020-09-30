def generation_based(ga):
    """Generation based approach to termination - If the current generation is
    less then the """
    status = True
    if(ga.current_generation > ga.max_generations):
        status = False
    return status
