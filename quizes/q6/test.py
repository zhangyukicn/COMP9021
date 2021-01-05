'''
'''
'''
R = 4
C = 4
def maxHist(row):
    result = []
    top_val = 0
    max_area = 0
    area = 0
    i = 0
    while (i < C):
        if (len(result) == 0) or (row[result[0]] <= row[i]):
            result.append(i)
            i += 1
        else:
            top_val = row[result[0]]
            result.pop(0)
            area = top_val * i
            if (len(result)):
                area = top_val * (i - result[0] - 1 )
            max_area = max(area, max_area)
    while (len(result)):
        top_val = row[result[0]]
        result.pop(0)
        area = top_val * i
        if (len(result)):
            area = top_val * (i - result[0] - 1 )

        max_area = max(area, max_area)

    return max_area

def maxRectangle(A):
    result = maxHist(A[0])
    for i in range(1, R):
        for j in range(C):
            if (A[i][j]):
                A[i][j] += A[i - 1][j]
        result = max(result, maxHist(A[i]))

    return result
if __name__ == '__main__':
    A = [[0, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 1],
         [1, 1, 0, 0]]

    print("Area of maximum rectangle is", maxRectangle(A))

from random import seed, randrange
import sys

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)


def size_of_largest_parallelogram_third(point, size):
    #      111
    #     111
    #    111
    #   111
    # get the current point
    (x, y) = point
    # check current row and next row
    for height in range(0, 2):
        for width in range(0, size):

            current_x = x + height + width
            current_y = y + height

            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return 0

    # if current row and next row are all 1
    for height in range(2, len(grid) - y):
        for width in range(0, size):
            current_x = x + height + width
            current_y = y + height
            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return height * size

    # last line
    return (dim - y) * size


def size_of_largest_parallelogram_two(point, size):
    #      111
    #     111
    #    111
    #   111
    # get the current point
    (x, y) = point
    # check current row and next row
    for height in range(0, 2):
        for width in range(0, size):

            current_x = x - height + width
            current_y = y + height

            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return 0
    # if current row and next row are all 1
    for height in range(2, len(grid) - y):
        for width in range(0, size):
            current_x = x - height + width
            current_y = y + height
            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return height * size

    # last line
    return (dim - y) * size


def size_of_largest_parallelogram_one(point, size):
    #      111
    #      111
    #      111
    #      111
    # get the current point
    (x, y) = point
    # check current row and next row
    for height in range(0, 2):
        for width in range(0, size):

            current_x = x + width
            current_y = y + height

            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return 0
    # if current row and next row are all 1
    for height in range(2, dim - y):
        for width in range(0, size):
            current_x = x + width
            current_y = y + height
            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return height * size

    # if last line
    return (dim - y) * size


def size_of_largest_parallelogram():
    # REPLACE PASS ABOVE WITH YOUR CODE
    # check current position is 1
    max_size = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                # 1 1 0 0000 1 11
                for size in range(2, dim - x):
                    # check the star length 2
                    first = size_of_largest_parallelogram_one((x, y), size)
                    second = size_of_largest_parallelogram_two((x, y), size)
                    third = size_of_largest_parallelogram_third((x, y), size)
                    max_size = max((max_size, first, second, third))

    return max_size


# POSSIBLY DEFINE OTHER FUNCTIONS

def get_max(line, index, type=1):

    y, x = divmod(index, dim)
    result = 0
    for step in range(2, dim - x):
        height = 0
        temp = index
        y, x = divmod(index, dim)
        while temp < len(line) and line[temp: temp + step] == "1" * step:
            height += 1
            if type == 1:
                temp = (y + 1) * dim + x
            elif type == 2:
                if x == 0:
                    break
                temp = (y + 1) * dim + x - 1
            else:
                if x + 1 == dim:
                    break
                temp = (y + 1) * dim + x + 1
            y, x = divmod(temp, dim)
        if height > 1:
            result = max(result,height * step)
        else:
            break
    return  result


def size_of_largest_parallelogram_ext():
    line = "".join([str(x) for row in grid for x in row])

    max_size = 0
    for index in range(len(line)):
        if line[index] == "1":
            max_size = max(max_size,get_max(line,index,1))
            max_size = max(max_size,get_max(line, index, 2))
            max_size = max(max_size,get_max(line, index, 3))
    return max_size


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
size = size_of_largest_parallelogram_ext()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
          )
else:
    print('There is no parallelogram with horizontal sides.')
'''

grid = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1]]

def search(i,j,c):
    if 0<=i <10 and 0<= j<10 and grid[i][j]==1:
        grid[i][j] =c
        for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
            search(i+x,j+y,c)
    else:
        return
c = 2
for i in range(10):
    for j in range(10):
        if grid[i][j]:
            search(i,j,c)
            c += 1

print(grid)
