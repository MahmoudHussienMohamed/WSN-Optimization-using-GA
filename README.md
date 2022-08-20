# WSN-Optimization-using-GA
Sensor placement in a network using **Genetic Algorithm** properties.

## What's Genetic Algorithm?
*GA* is an algorithm inspierd from Darwin's theory of natural evolution and the mechanism of natural selection. Consider a society `(population)` contains arbitrary number of individuals; Two individuals `(parents)` bred and had two `children` they would have the genes and features of their parents with the probability of `mutation` (have extra feature or abandon inherited one). Children would grow and became a part of the society `(population)` and repeat the process for fittest individuals (highest `scores`) and have higher ability to servive and pass their genes or features to thier progeny.

## How GA simulates natural selection mechanism?
- At first, We start with initial random `population`.
- Fittest ones (highest `scores`) have higher probability to live and breed.
- Each couple from fittest ones (`parents`) breed and produce children with mixed features from both of them.
- Weak individuals extinects and replaced with better `generation`.
- repeat the process untill the goal reached.
Pseudo Code:
```
population <- Random Population
Repeat N times or untill goal is reached:
    scores <- calculate_score_of(individual) For all individuals in population
    selected <- list of fittest individuals in population
    for parent1, parent2 in seleted:
        child1, child2 = breedAndCrossOver(parent1, parent2)
        with mutationRate probability:
          changeFeatureFor(child1 or child2)
        newPopulation.add(child1)
        newPopulation.add(child2)
    population <- newPopulation
```

