import numpy as np
import argparse
import sys
from multiprocessing import Pool

np.random.seed(2021)

#@profile
def inside_circle(total_count):
  x = np.float32(np.random.uniform(size=total_count))
  y = np.float32(np.random.uniform(size=total_count))
  radii = np.sqrt (x*x + y*y)
  filtered = np.where(radii <= 1.0)
  count = len(radii[filtered])
  return count

def estimate_pi(total_count,n_cores):
  partitions = [ ]
  for i in range(n_cores):
    partitions.append(int(total_count/n_cores))

  pool = Pool(processes=n_cores)
  counts = pool.map(inside_circle, partitions)
  total_count = sum(partitions)
  return (4.0 * sum(counts) / total_count )


def main():
  parser = argparse.ArgumentParser(
          description='Estimate Pi using a Monte Carlo method.')
  parser.add_argument('n_samples', metavar='N', type=int, nargs=1,
          default=10000,
          help='number of times to draw a random number')
  parser.add_argument('n_cores', metavar='N', type=int, nargs=1,
          default=1,
          help='number of cores to use')
  args = parser.parse_args()

  n_samples = args.n_samples[0]
  n_cores = args.n_cores[0]
  my_pi = estimate_pi(n_samples,n_cores)

  print("[serial version] pi is %f from %i samples with %i" % (my_pi, n_samples,n_cores))
  sys.exit(0)

if __name__=='__main__':
  main()
