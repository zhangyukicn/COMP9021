import math
import sys
from random import seed, randint
import numpy


try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
seed(arg_for_seed)
L = [randint(-50, 50) for _ in range(nb_of_elements)]
print('The list is:',L)

sum = 0
for i in L:
    sum = i + sum
    average = sum/len(L)
print('The mean is:',f'{average:7.2f}')

L = sorted(L)
if len(L) % 2 ==0:
    a = len(L) // 2
    b = (len(L) - 1) // 2
    median = (L[a]+L[b])/2
else:
    c = len(L) // 2
    median = L(c) /2
print('The median is:',f'{median:7.2f}')

another_sum = 0
for x in range(0,len(L)):
   another_sum = another_sum + pow((L[x] - average),2)
   standard_deviation = math.sqrt((another_sum/len(L)))
print('The standard deviation is',f'{standard_deviation:7.2f}')

print(numpy.var(L))



















