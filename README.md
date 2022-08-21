# WSN-Optimization-using-GA
Sensor placement in a network using **Genetic Algorithm** properties.

## What's Genetic Algorithm?
*GA* is an algorithm inspierd from Darwin's theory of natural evolution and the mechanism of natural selection. Consider a society (`population`) contains arbitrary number of individuals; Two individuals (`parents`) bred and had two `children` they would have the genes and features of their parents with the probability of `mutation` (have extra feature or abandon inherited one). Children would grow and became a part of the society (`population`) and repeat the process for fittest individuals (highest `scores`) and have higher ability to servive and pass their genes or features to thier progeny.

## How GA simulates natural selection mechanism?
- At first, We start with initial random `population`.
- Fittest ones (highest `scores`) have higher probability to live and breed.
- Each couple from fittest ones (`parents`) breed and produce children with mixed features from both of them.
- Weak individuals extinects and replaced with better `generation`.
- repeat the process untill the goal reached.
### Pseudo Code:
```
population <- Random Population
Repeat N times or untill goal is reached:
    scores <- calculate_score_of(individual) For all individuals in population
    selected <- list of fittest individuals in population
    for parent1, parent2 in seleted:
        child1, child2 <- breedAndCrossOver(parent1, parent2)
        with mutationRate probability:
          changeFeatureFor(child1 or child2)
        newPopulation.add(child1)
        newPopulation.add(child2)
    population <- newPopulation
```
## setup
Make sure that `numpy` and `tkinter` are installed. Use `pip install numpy` and `pip install tkinter`; if they're not installed they will be downloaded and installed.
Then, run `python Runner.py 100 10 20 20` you will be able to see something like this:
<br /><br />
![](https://github.com/MahmoudHussienMohamed/WSN-Optimization-using-GA/blob/main/Images/Output.jpg)
<br />

## Project specfication and description:
Applying Genetic Algorithm concepts to find the best placement for sensors in Sensor netowrk. Each sensor had position (`X`, `Y`) and `radius` descriping its domain. We represent sensor as `chromosome` or string of features to manipulate. After all the process is done we can visulaize generations to see how it did. 
## Code Walkthrough and Logic
There're three Modules:
- [GeneticAlgorithm.py](https://github.com/MahmoudHussienMohamed/WSN-Optimization-using-GA/blob/main/GeneticAlgorithm.py): Which contains all the logic for genetic algorithm,
- [CoverageArea.py](https://github.com/MahmoudHussienMohamed/WSN-Optimization-using-GA/blob/main/CoverageArea.py): to calculate the objective function or fitness score ,
- [DrawSensors.py](https://github.com/MahmoudHussienMohamed/WSN-Optimization-using-GA/blob/main/DrawSensors.py): handles GUI and buttons to display sensors
and driver code:
- [Runner.py](https://github.com/MahmoudHussienMohamed/WSN-Optimization-using-GA/blob/main/Runner.py): firing the **GeneticAlgorithm** Module and call **DrawSensors** with GA object. 
### GeneticAlgorithm:
There's main class `GeneticAlgorithm` has bunch of attributes: `iterationsNo` or generation number, `populationNo` population size, `bitsNo` number of bits per individual in population, `cross_over_rate` can be considered as the probability to have a crossover, `mutation_rate` probability for mutation to occure, `sensors_radius` the radius of the sensor caoverage, `population` sensors locations, `best_gen` fittest generation index, `best_score` highest covered area so far, `generations` list of populations (society within an era) and finaly, `coverage` list of total coverage areas per generation. 
And some methods such as `init_population` which initiate population, `objective` to calculate the fitness score, `select` to select fit individual, `cross_over` to reproduce two children from two selected parents, `mutation` to mutate random feature for child and main method `start` which fires logic by calling all of them.

As I discussed about [Genetic Algorithm](https://github.com/MahmoudHussienMohamed/WSN-Optimization-using-GA#how-ga-simulates-natural-selection-mechanism) we apply steps as follow:
- Initiate random population.
- Record coverage area for sensors (fitness score).
- Select two fit parents to breed and reproduce two children have traits of them with probability to mutate.
- Do all of above for all parents untill the compeletion for generation then start with last population.

### CoverageArea:
Simple module to calculate the total coverage area for sensors and corresponding area for each one to calculate the fitness score by traversing all points (pixels) in the plane and count covered one.

### DrawSensors:
GUI tkinter window to display sensors as generations given **GeneticAlgorithm** object *GA*. See [this](https://docs.python.org/3/library/tkinter.html) if unfamiliar with tkinter.

## Notes:
- This project may not be the most suitable or direct application of Genetic Algorithm but nice start to understand.
- Perfomance is pretty bad so, enhancements are coming soon.

## Refrences:
[Machine Learning Mastery article](https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/) from the fascinating Jason Brownlee.

