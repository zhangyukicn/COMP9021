# COMP9021 19T3 - Rachid Hamadi
# Quiz 1 *** Due Thursday Week 2


import sys
from random import seed, randrange


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []
# INSERT YOUR CODE HERE
exist_key = []
exist_value = []

for key in mapping.keys():
    exist_key.append(key)

for value in mapping.values():
    exist_value.append(value)

for except_number in range(1,upper_bound):
    if except_number not in exist_key:
        nonkeys.append(except_number)

mapping_as_a_list = [None] * upper_bound
for x in exist_key:
    mapping_as_a_list[x] = mapping[x]

no_repetitive_value =[]
for y in exist_value:
    if exist_value.count(y) == 1:
        no_repetitive_value.append(y)

for w in no_repetitive_value:
    A = exist_value.index(w)
    B = exist_key[A]
    one_to_one_part_of_mapping[B] = w


print()
print('The mappings\'s so-called "keys" make up a set whose number of elements is',str(len(exist_key))+'.')
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.

one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                      for key in sorted(one_to_one_part_of_mapping)
                             }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)


