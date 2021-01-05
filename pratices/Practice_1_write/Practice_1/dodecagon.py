


'''
Draws a dodecadon with the colour of each sector alternating red and blue.
'''


from turtle import *


edge_length = 100
angle = 30


def draw_triangle(i, colour):
    color(colour) #颜色
    begin_fill() #开始填充
    goto(vertices[i]) #前往 i
    goto(vertices[i + 1]) #前往 i + 1
    end_fill() #结束填充


vertices = []
penup() #画笔抬起
# Determine the positions of the 12 vertices of the dodecagon
# by going to each of them (moving a distance of 100 from the origin,
# in a direction of 0, -30, -60, -90,... degrees), recording the position,
# and appending that position to the list vertices.
# So vertices is eventually the list
# [(x_0, y_0), (x_1, y_1), (x_2, y_2),..., (x_{11}, x_{11})] where
# (x_i, y_i) are the x and y coordinates of the (i+1)st vertice.
for i in range(12):
    right(i * angle) #右转
    forward(edge_length)
    vertices.append(pos())
    # A shortchut for: get back to the origin
    home()
# Add to the end of the list vertices the coordinates of the first vertice
# in order to "close" the picture. So vertices becomes
# [(x_0, y_0), (x_1, y_1), (x_2, y_2),..., (x_{11}, x_{11}), (x_0, y_0)].
vertices.append(vertices[0])    
pendown()
for i in range(12):
    home()
    # If i is odd because the division of i by 2 yields a remainder of 1
    # then make colour 'red'; otherwise make it 'blue'.
    colour = 'red' if i % 2 else 'blue'
    draw_triangle(i, colour)
