import EasyGA
import random

#Create the Genetic Algorithm
ga = EasyGA.GA()
password = input("""Please enter a word or sentence (Use only standard
 characters such as letters, spaces and, punctuation marks): """)
ga.chromosome_length = len(password)
ga.fitness_goal = len(password)

ga.population_size = 50
ga.generation_goal = 1000


def password_fitness(chromosome):

    fitness = 0

    # For each gene in the chromosome
    for gene, letter in zip(chromosome, password):

        # If the gene letter matchs the password
        if gene.value == letter:
            fitness += 1

    return fitness


ga.fitness_function_impl = password_fitness

ga.adapt_population_flag = False
ga.adapt_rate = 0

# Creates random genes utilizing the characters below
ga.gene_impl = lambda: random.choice([
"A","a","B","b","C","c","D","d","E","e",
"F","f","G","g","H","h","I","i","J","j",
"K","k","L","l","M","m","N","n","O","o",
"P","p","Q","q","R","r","S","s","T","t",
"U","u","V","v","W","w","X","x","Y","y",
"Z","z"," ",".","!","?"])

ga.evolve()

#Print your default genetic algorithm
ga.print_generation()
ga.print_population()

#Prints a graph of the genetic algorithm
ga.graph.highest_value_chromosome()
ga.graph.show()
