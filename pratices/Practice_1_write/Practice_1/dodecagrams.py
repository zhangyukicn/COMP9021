


'''
Draws three coloured dodecagrams, separed by a distance of one third
the length of the edges, and centred in the window that displays them.
'''


from turtle import color,begin_fill,forward,left,end_fill,penup,pendown




edge_length = 150
angle = 150


def draw_dodecagram(colour):
    color(colour) #颜色
    begin_fill()  #开始填充
    for _ in range(12):
        forward(edge_length) #前进
        left(angle)  #右转
    end_fill()  #结束 填充

def teleport(distance):
    penup()    #画笔抬起
    forward(distance) #前进
    pendown() #画笔放下


# Make sure that the dodecagrams are centred horizontally in the window that displays them.
# Without the following statement, the left end of the horizontal edge of the green dodecagram,
# from which the drawing starts, would be at the centre of the screen
# (so the dodecagrams are not quite centred vertically).
teleport(- edge_length // 2)
# Draw the middle dodecagram, then the left dodecagram, then the right dodecagram.
draw_dodecagram('green')
teleport(- 4 * edge_length // 3)
draw_dodecagram('red')
teleport(8 * edge_length // 3)
draw_dodecagram('blue')
