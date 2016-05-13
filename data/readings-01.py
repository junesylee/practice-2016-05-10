import sys
import numpy
def main():
   filename = sys.argv[1]
   data = numpy.loadtxt(filename, delimiter=',')
   for m in data.mean(axis=1): 
       print(m)
main () 

