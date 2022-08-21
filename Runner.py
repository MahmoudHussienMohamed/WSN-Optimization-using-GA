from GeneticAlgorithm import GeneticAlgorithm
from DrawSensors import window
import sys

def main():
    if len(sys.argv) != 5:
        sys.exit("Usage: python Runner.py [ITERATION_NUMBER] [POPULATION_NUMBER] [BITS_NUMBER] [SENSOR_RADIUS]")
    n_iter, n_pop, n_bits, radius = map(int, sys.argv[1:])
    cross_r = 0.9
    mut_r = 1.0 / n_bits
    GA = GeneticAlgorithm(n_iter, n_pop, n_bits, cross_r, mut_r, radius)
    GA.start()
    win = window(GA)
    win.show()
    
if __name__ == '__main__':
    main()
