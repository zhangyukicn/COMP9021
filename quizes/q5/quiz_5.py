# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys


def encode(list_of_integers):#[10, 20, 30]
    str_of_integers =( f'{", ".join(bin(e)[2: ] for e in the_input)}')
    str_of_integers=str_of_integers.replace(',','#')
    str_of_integers=str_of_integers.replace(' ','')
    #print(str_of_integers)
    list_of_integers = list(str_of_integers)
    str_list_of_integers = ''
    for i in range(0,len(list_of_integers)):
        str_list_of_integers = str_list_of_integers + list_of_integers[i] * 2
    #print(str_list_of_integers )
    str_list_of_integers = str_list_of_integers.replace('##','0')
    return str(int(str_list_of_integers, 2))

def decode(the_input):
    Wrong = 'Incorrect encoding!'
    list_the_input = list(str(bin(the_input)[2 :]))
    a = []
    i = 0
    while len(list_the_input)!= 0:
        if list_the_input[i] == list_the_input[i+1]:
            a.append(list_the_input[i])
            list_the_input.remove(list_the_input[i])
            list_the_input.remove(list_the_input[i])
        elif list_the_input[i] != list_the_input[i+1] and (list_the_input[i] == '0' and list_the_input[i+1]=='1'):
            a.append(',')
            list_the_input.remove(list_the_input[i])
        elif list_the_input[i] != list_the_input[i+1] and (list_the_input[i] == '1' and list_the_input[i+1]=='0'):
            return Wrong

    #print(a)
    number = ''
    list_number =[]
    for i in range(0,len(a)):
        if a.count(',')== 0:
            int_a = ''.join(a)
            return [int(str(int(int_a, 2)))]
        else:
            if a[i] !=',':
                number = number + a[i]
            else:
                list_number.append(number)
                number=''
    list_number.append(number)
    return [int(str(int(i, 2))) for i in list_number]


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))#eval() 函数用来执行一个字符串表达式，并返回表达式的值
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
