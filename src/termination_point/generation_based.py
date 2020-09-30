def generation_based(ga):
    status = True
    if(ga.current_generation > ga.max_generations):
        status = False
    return status
