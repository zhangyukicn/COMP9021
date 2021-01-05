import math

def first_computation(A):
    i = 0
    while A % 10 == 0:
        i = i + 1
        A = A // 10
    return 'Computing the number of trailing 0s in 15! by dividing by 10 for long enough: {}'.format(i)

def second_computation(A):
    A = list(str(A))
    list_A = list(map(int,A))
    #print(list_A)
    number = 0
    for i in range(len(list_A)-1,0,-1):
        if list_A[i] == 0:
            #print(list_A[i])
            number = number + 1
            continue
        else:
            break
    return 'Computing the number of trailing 0s in 15! by converting it into a string: {}'.format(number)

def third_computation(A):
    nb_of_trailing_0s = 0
    power_of_five = 5
    while A >= power_of_five:
        nb_of_trailing_0s += A // power_of_five
        power_of_five *= 5
    return 'Computing the number of trailing 0s in 345! the smart way: {}'.format(nb_of_trailing_0s)













try:
    random_number = int(input('Input a nonnegative integer :'))
    if random_number <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
A = math.factorial(random_number)
print(first_computation(A))
print(second_computation(A))
print(third_computation(random_number))









#method 2
'''
try:
    random_number = int(input('Input an integer at least equal to 5:'))
    if random_number <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
A = math.factorial(random_number)
b = list(str(A))
c = b.count('0')
i = 1
if()
'''



