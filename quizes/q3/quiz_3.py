# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys


on = '\u26aa' #(白圈)
off = '\u26ab' #（黑圈）
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
number = '0' * nb_of_leading_zeroes + f'{int(code):o}.'
#print(number)
number_list = []

#print(begin)
for i in range(len(number)):
    #print(number[i])
    number_list.append(number[i])
#print(number_list)
del number_list[-1]
#print(number_list)
number_list = list(reversed(number_list))
number_list = list(map(int, number_list))
#print(number_list)

all_number =[(0,0)]
x,y = 0,0
for i in number_list:
    if i == 0:
        x = x
        y = y + 1
        all_number.append((x,y))
    elif i == 1:
        x = x + 1
        y = y + 1
        all_number.append((x,y))
    elif i == 2:
        x = x + 1
        y = y
        all_number.append((x,y))
    elif i ==3:
        x = x + 1
        y = y - 1
        all_number.append((x,y))
    elif i ==4:
        x = x
        y = y - 1
        all_number.append((x,y))
    elif i ==5:
        x = x -1
        y = y -1
        all_number.append((x,y))
    elif i ==6:
        x = x -1
        y = y
        all_number.append((x,y))
    elif i ==7:
        x = x - 1
        y = y + 1
        all_number.append((x,y))
#print(all_number)

B = []
C = []
a1 = []
for i in range(len(all_number)):
    if all_number.count(all_number[i]) % 2 == 0:
        B.append(all_number[i])
#print(B)
for y in all_number:
    if y not in B or y in a1:
        C.append(y)
        a1 = sorted(set(C),key=C.index)
#print('C',C)
#print('delete multiple:',a1)

if len(a1) != 0:
    x_row, y_cloum = zip(*a1)
    x_row = sorted(set(sorted(x_row)),key=sorted(x_row).index)
    y_cloum =list(reversed(sorted(set(sorted(y_cloum)),key=sorted(y_cloum).index)))
    x_row_count = [i for i in range(x_row[0],x_row[-1]+1)]
    y_cloum_count = list(reversed([j for j in range(y_cloum[-1],y_cloum[0]+1)]))
    print(x_row_count)
    print(y_cloum_count)


    print('x_row',x_row)
    print('y_cloum',y_cloum)

    for y in y_cloum_count:
        for x in x_row_count:
            if(x,y) not in a1:
                print(off,end ='')
            else:
                print(on,end ='')
        print()
input('qewsdss')

