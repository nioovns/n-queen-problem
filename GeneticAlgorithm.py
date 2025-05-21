import random

Count_Of_Individual = 500
Max_generation = 5000
Mutation_rate = 0.3
Tournament_size = 5 

#this method for create cromosom
class creat_cromosom:
    def __init__(self, n):
        self.genes = list(range(1, n+1))
        random.shuffle(self.genes)
        self.fitness = self.calculate_fitness(n)

    
    def calculate_fitness(self, n):
        countOfCollicions = 0
        for i in range(n):
            for j in range(i+1, n):
                if abs(self.genes[i] - self.genes[j]) == abs(i-j):
                    countOfCollicions += 1
        return countOfCollicions



def select(population):
    candidates = random.sample(population, Tournament_size)
    return min(candidates, key=lambda c: c.fitness)


def crossover(parent1, parent2, n):
    cutpoint = random.randint(0, n-1)
    child_genes = parent1.genes[:cutpoint]
    used = set(child_genes)

    for gene in parent2.genes:
        if gene not in used:
            child_genes.append(gene)
            used.add(gene)

  
    if len(child_genes) < n:
        remaining = [g for g in range(1, n+1) if g not in used]
        child_genes += remaining

    child = creat_cromosom(n)
    child.genes = child_genes
    child.fitness = child.calculate_fitness(n)
    return child


def mutate(chrom, n):
    if random.random() < Mutation_rate:
        i, j = random.sample(range(n), 2)
        chrom.genes[i], chrom.genes[j] = chrom.genes[j], chrom.genes[i]
        chrom.fitness = chrom.calculate_fitness(n)


def initial_population(n):
        
    return [creat_cromosom(n) for _ in range(Count_Of_Individual)]

def genetic_algorithm(n):
    population = initial_population(n)

    for generation in range(Max_generation):
        population.sort(key=lambda c: c.fitness)

        if generation % 100 == 0:
            print(f"Generation {generation}: Best fitness = {population[0].fitness}")

        if population[0].fitness == 0:
            print("\nSolution Found!")
            print(f"Generation: {generation}")
            print("Genes:", population[0].genes)
            print("Fitness:", population[0].fitness)
            return population[0]

        new_population = []
        for _ in range(Count_Of_Individual):
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2, n)
            mutate(child, n)
            new_population.append(child)

        population = new_population

    return None


