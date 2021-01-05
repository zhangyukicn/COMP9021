from random import seed, randrange
import sys
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
L = [randrange(0,19) for _ in range(nb_of_elements)]
print('\nThe list is:' , L)
remainders_modulo_5 = [0] * 5
for x in L:
    remainders_modulo_5[x // 5] += 1
print(remainders_modulo_5)

for r in range(0,6):
    if remainders_modulo_5[r] == 0:
        L1 ='There is no element'
    elif remainders_modulo_5[r] == 1:
        L1 ='There is 1 element'
    else:
        L1 ='There are',{remainders_modulo_5[r]},'elements'














