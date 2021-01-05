 # COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
exist_key = []
exist_value = []
L = []
for key,value in mapping.items():
    exist_key.append(key)
    exist_value.append(value)
    if key == value:
        L.append([key])
#print('exist_key:                 ',exist_key )
#print('mapping[i] or exist_value:',exist_value)
#print('L:',L)

for i in range(len(mapping)):
    for x in exist_key:
        if exist_value[i] == x:
            L2 = []
            out_cycle = exist_value[i]
            L2.append(exist_key[i])
            L2.append(exist_value[i])
            #print(L2)
            while out_cycle in exist_key:
                A = exist_key[exist_key.index(out_cycle)]
                L2.append(A)
                B = exist_value[exist_key.index(out_cycle)]
                L2.append(B)
                out_cycle = B
                if len(L2) > len(exist_key):
                    break
                #print('L2：',L2)
                if L2[0] == L2[-1]:
                    C = list(L2)
                    C1 = sorted(set(C),key=C.index)
                    #print('c;',C1)
                    if C1 not in L:
                        L.append(C1)
                        break
                    #print(L)
listkk =[]
listkkk=[]
cycles = sorted(L)
#print('cycles',cycles)
for x in range(len(cycles)):
    for y in range(x,len(cycles)):
        if x ==y :
            continue
        elif set(cycles[x]) ==set(cycles[y]):
            listkkk.append(cycles[y])
            #print('listkkk',listkkk)
for x in range(len(cycles)):
    if cycles[x] not in listkkk:
        listkk.append(cycles[x])
cycles=listkk






dict = {}
temp_dict1 = {}
list1 =[]
for key in exist_value:
    dict[key] = dict.get(key, 0) + 1
#print(dict)

temp_dict1 = {}
for values in exist_value:
    L4 = []
    for keys in exist_key:
        if mapping[keys] == values:
            L4.append(keys)
            #print(L4)
    temp_dict1[values] = L4
#print(temp_dict1)

temp_dict = {}
for keys,number in dict.items():
    for x,y in temp_dict1.items():
        if keys == x:
            temp_dict.setdefault(number,{x:y})
            #print('reversed_dict_per_length',temp_dict)
            temp_dict[number].update({x:y})
            #print('temp_dict[number]',temp_dict)
reversed_dict_per_length = temp_dict



print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


