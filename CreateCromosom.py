import random

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