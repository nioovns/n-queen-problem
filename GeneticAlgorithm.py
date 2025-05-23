import random
from CreateCromosom import creat_cromosom

Count_Of_Individual = 500
Max_generation = 5000
Mutation_rate = 0.3
Tournament_size = 5 

def select_parent(population):
    candidates = random.sample(population, Tournament_size)   #5 chromosomes are chosen randomly
    return min(candidates, key=lambda c: c.fitness)     #The chromosome with the lowest fitness

#This method for combination of parent1 and parent2
def crossover(parent1, parent2, n):
    cutpoint = random.randint(0, n-1)                              #Randomly select index list       
    child_genes_of_parent1 = parent1.genes[:cutpoint]              #Getting the genes of the parent1 according to the cut point
    used = set(child_genes_of_parent1)                             #The genes we inherited from our parent1 

    for gene in parent2.genes:
        if gene not in used:
            child_genes_of_parent1.append(gene)
            used.add(gene)

  
    if len(child_genes_of_parent1) < n:
        remaining = [g for g in range(1, n+1) if g not in used]
        child_genes_of_parent1 += remaining

    child = creat_cromosom(n)
    child.genes = child_genes_of_parent1
    child.fitness = child.calculate_fitness(n)
    return child


def mutate(chrom, n):
    if random.random() < Mutation_rate:
        i, j = random.sample(range(n), 2)
        chrom.genes[i], chrom.genes[j] = chrom.genes[j], chrom.genes[i]    #Transposition of 2 genes
        chrom.fitness = chrom.calculate_fitness(n)

#crearte population
def initial_population(n):
        
    return [creat_cromosom(n) for _ in range(Count_Of_Individual)]

def genetic_algorithm(n):
    population = initial_population(n)

    for generation in range(Max_generation):
        population.sort(key=lambda c: c.fitness)                        #sort of population base on their fitness

        if population[0].fitness == 0:
            return population[0]

        new_population = []
        for _ in range(Count_Of_Individual):
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child = crossover(parent1, parent2, n)
            mutate(child, n)
            new_population.append(child)

        population = new_population

    return None


