# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys


dim = 10


def display_grid():# 10 * 10 pic #1 4
    for row in grid:
        print('   ', *row)
    #print(len(grid))
    #print(grid[0][0])
    print(grid[0][0],grid[0][1])


def size_of_largest_parallelogram():
    pass
    # REPLACE PASS ABOVE WITH YOUR CODE
def function_direction():
    pass

def main_function_grid():
    zero_sum = 0
    one_sum = 0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if grid[i][j] == 0:
                zero_sum = zero_sum + 1
            else:
                for k in range(0,10-j):
                   first = max(0, the_first_function(i,j,k))
                   second = max(0, the_second_function(i,j,k))
                   third =  max(0,the_third_function(i,j,k))
                   max_size = max(first,second,third)
    print(zero_sum,one_sum)
    print('the_max_size_is {}'.format(max_size))

def the_first_function(i,j,k):
    #2 个
    next_grid =grid[i][j+1]
    if grid[i][j+1] == 0:
        pass

    '''
    11
    11
    11
    '''
    '''
    direction_x_y= {'point':(0,0),'up':(-1,0),'左上':(-1,-1),'右上':(-1,1),'左':(0,-1),
                    '右':(0,1),'zuoxia':(1,-1),'右下':(1,1),'xia':(1,0)}
    if i == 0 and j == 0:
    '''


def the_second_function(i,j,k):
    pass

def the_third_function(i,j,k):
    pass





# POSSIBLY DEFINE OTHER FUNCTIONS



try:
    
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')
