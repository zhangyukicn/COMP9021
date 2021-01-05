from turtle import *

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

teleport(- edge_length // 2)
teleport(- 4 * edge_length // 3)
teleport(8 * edge_length // 3)


