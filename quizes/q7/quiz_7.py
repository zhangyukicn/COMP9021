# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys
from collections import defaultdict

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.

location ={'up':(-1,0),'down':(1,0),'left':(0,-1),'right':(0,1)}
ten = [i for i in range(0,dim)]
ten_1 = [j for j in range(0,dim)]

def deep_search(i,j,colour):
    if i in ten and j in ten_1:
        if grid[i][j]== 1:
            grid[i][j] = colour
            for k in location.values():
                x,y =k
                new_x = i+x
                new_y = j+y
                deep_search(new_x,new_y,colour)
        elif grid[i][j]== 0:
            return

def colour_shapes():
    colour = 2
    pic = defaultdict(list)
    for i in range(0,dim):
        for j in range(0,dim):
            if grid[i][j]== 1: #find color
                deep_search(i,j,colour)
                colour = colour + 1
            if grid[i][j]> 0: # find the point belong to color
                pic[grid[i][j]].append((i,j))
    return pic


def max_number_of_spikes(nb_of_shapes):
    pass
    # Replace pass above with your code


# Possibly define other functions here    


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
#nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
     # max_number_of_spikes(nb_of_shapes)
     )


colour = 2
pic = defaultdict(list)
for i in range(0,dim):
    for j in range(0,dim):
        if grid[i][j]== 1: #find color
            deep_search(i,j,colour)
            colour = colour + 1
        if grid[i][j]> 0: # find the point belong to color
            pic[grid[i][j]].append((i,j))
print(grid)
print(pic)


count = 0
for k in pic:
    for d in pic[k]:
        i,j = d
        if i in ten and j in ten_1:
            for z in location.values():
                x,y = z
                new_x = i +x
                new_y = i +y
                if grid[new_x][new_y] == 0:
                    count = count + 1
                    #print(count)













