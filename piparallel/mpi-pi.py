import numpy as np
import sys
import datetime
from mpi4py import MPI

def inside_circle(total_count):
  x = np.random.uniform(size=total_count)
  y = np.random.uniform(size=total_count)
  radii = np.sqrt(x*x + y*y)
  count = len (radii[np.where(radii<=1.0)])
  return count

def main():
  comm = MPI.COMM_WORLD
  size = comm.Get_size()
  rank = comm.Get_rank()
  n_samples = int(sys.argv[1])
  my_samples = n_samples//size + ( N % size > rank)

  my_start_time = MPI.Wtime()
  my_counts = inside_circle(my_samples)
  counts = comm.reduce(my_counts,op=MPI.SUM,root=0)
  my_end_time = MPI.Wtime()
  my_elapsed_time = my_end_time - my_start_time
  max_elapsed_time = comm.reduce(my_elapsed_time,op=MPI.MAX,root=0)
  my_pi = 4.0 * counts / n_samples
  if rank == 0:
    print("Pi: {}, time: {} s".format(my_pi,max_elapsed_time))

if __name__ == '__main__':
  main()
