import sys
try:
    a = input('Input an integer')
    if int(a) < 0:
        raise ValueError
except ValueError:
    print('INcorrect writing,give up')
    sys.exit()


def perfect_function(x):
    L =[]
    for i in range(1,x-1):
        if x%i ==0:
            L.append(i)
    if sum(L) == x:
        return True

for x in range(1,int(a)+1):
    if perfect_function(x) == True:
        print('{} is a perfect number.'.format(x))



