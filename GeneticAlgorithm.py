from numpy.random import randint, rand
import CoverageArea

class GeneticAlgorithm:
    def __init__(self, n_iter, n_pop, n_bits, cross_r, mut_r, radius):
        self.iterationsNo = n_iter
        self.populationNo = n_pop
        self.bitsNo = n_bits
        self.cross_over_rate = cross_r
        self.mutation_rate = mut_r
        self.sensors_radius = radius
        self.init_population()
    
    def init_population(self):
        self.population = [randint(0, 2, self.bitsNo).tolist() 
            for _ in range(self.populationNo)]
    
    def objective(self):
        return CoverageArea.calculate(self.population, self.bitsNo, self.sensors_radius)

    def select(self, scores, k = 3):
        selected = randint(self.populationNo)
        for i in randint(0, self.populationNo, k - 1):
            if scores[i] > scores[selected]:
                selected = i
        return self.population[selected]

    def cross_over(self, parent1, parent2):
        child1, child2 = parent1, parent2
        if rand() < self.cross_over_rate:
            split_point = randint(1, len(parent1) - 2)
            child1 = parent1[:split_point] + parent2[split_point:]
            child2 = parent2[:split_point] + parent1[split_point:]
        return child1, child2

    def mutation(self, bitstring):
        for i in range(len(bitstring)):
            if rand() < self.mutation_rate:
                bitstring[i] = 1 - bitstring[i]
        return bitstring

    def start(self):
        self.population = [randint(0, 2, self.bitsNo).tolist() for _ in range(self.populationNo)]
        self.best_gen, self.best_score = 0, 0
        self.generations = [self.population]
        self.coverage = []
        for gen in range(self.iterationsNo):
            scores = self.objective()
            self.coverage.append(scores[0])
            scores = scores[1]
            if self.coverage[-1] > self.best_score:
                    self.best_gen, self.best_score = gen, self.coverage[-1]
            selected = [self.select(scores) for _ in range(self.populationNo)]
            childern = []
            for i in range(0, self.populationNo, 2):
                parent1, parent2 = selected[i], selected[i + 1]
                for c in self.cross_over(parent1, parent2):
                    childern.append(self.mutation(c))
            self.population = childern
            self.generations.append(childern)
        self.generations = [CoverageArea.convert_to_SENSOR(gen, self.bitsNo) for gen in self.generations]
        self.generations = [[[pop.x, pop.y] for pop in gen] for gen in self.generations]