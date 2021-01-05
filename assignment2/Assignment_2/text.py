from collections import defaultdict
import copy

'''
[[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1], 
 [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]
'''

def wall_find(find_wall_arry):
    list =[]
    for j in range(0,len(find_wall_arry)):
        L =[]
        for i in range(0,len(find_wall_arry[j])):
            if find_wall_arry[j][i] == 1:
                L.append((j,i))
            elif find_wall_arry[j][i] == 0 and len(L) > 1:
                list.append(L)
                L =[]
            else:
                L=[]
        if L!=[] and len(L)>1:
            list.append(L)
    #print(list)

    list_2 =[]
    for i in range(0,len(find_wall_arry[0])):
        L1 =[]
        for j in range(0,len(find_wall_arry)):
            if find_wall_arry[j][i] == 1:
                L1.append((j,i))
            elif find_wall_arry[j][i] == 0 and len(L1) > 1:
                list_2.append(L1)
                L1 =[]
            else:
                L1 =[]
        if L1!=[] and len(L1)>1:
            list_2.append(L1)
    #print(list_2)
    return list,list_2


def Entry_exit_paths(all_1_pictre_use_for_xuxina):
    L2=[]
    temp_pic_0 = all_1_pictre_use_for_xuxina[0]
    nb_of_shapes_ = colour_shapes_2(temp_pic_0)

    for x in range(0, len(gates_point[0])):
        L2.append(gates_point[0][x])

    ture_pic = defaultdict(list)
    for j in nb_of_shapes_:
        for i in nb_of_shapes_[j]:
            #print(i)
            y,x = i
            for z in L2:
                y1,x2 = z
                if y ==y1 and x==x2:
                    ture_pic[j].append((x,y))
    #print(ture_pic)

    keys =[]
    tem =[]
    for key,value in ture_pic.items():
        keys.append(key)
        if len(value)>2:
            #print(key)
            tem.append(key)
    #print(tem)

    #print(nb_of_shapes_)
    #print(A)
    for j in range(0,len(temp_pic_0)):
        for i in range(0,len(temp_pic_0[j])):
            if temp_pic_0[j][i] in tem:
                temp_pic_0[j][i] = 1
    #print(A)
    for j in range(0,len(temp_pic_0)):
        for i in range(0,len(temp_pic_0[j])):
            if temp_pic_0[j][i]!= 0 and temp_pic_0[j][i]!= 1:
                temp_pic_0[j][i] = 0
    print(temp_pic_0)

    list_a =[]
    for j in range(0,len(temp_pic_0)):
        L =[]
        for i in range(0,len(temp_pic_0[j])):
            if temp_pic_0[j][i] == 0:
                L.append((j,i))
            elif temp_pic_0[j][i] == 1 and len(L) > 1:
                list_a.append(L)
                L =[]
            else:
                L=[]
        if L!=[] and len(L)>1:
            list_a.append(L)
    #print(list_a)

    list_2 =[]
    for i in range(0,len(temp_pic_0[0])):
        L1 =[]
        for j in range(0,len(temp_pic_0)):
            if temp_pic_0[j][i] == 0:
                L1.append((j,i))
            elif temp_pic_0[j][i] == 1 and len(L1) > 1:
                list_2.append(L1)
                L1 =[]
            else:
                L1 =[]
        if L1!=[] and len(L1)>1:
            list_2.append(L1)
    #print(list_2)



    walls_list =[]
    uierui =[]
    for j in range(0,len(list_a)):
        walls_list =[]
        walls_list.append(list_a[j][0])
        walls_list.append(list_a[j][-1])
        uierui.append(walls_list)
    #print(uierui)
    use_xuxian =[]
    for j in range(0,len(uierui)):
        #print(uierui[j])
        for i in uierui[j]:
            y,x = i
            use_xuxian.append((x/2,y/2))
    #print(use_xuxian)
    odd_walls =[]
    even_walls =[]
    for x in range(0,len(use_xuxian)):
        if x %2 ==0:
            odd_walls.append(use_xuxian[x])
        else:
            even_walls.append(use_xuxian[x])
    #print(odd_walls)
    #print(even_walls)
    right_odd_walls =[]
    right_even_walls =[]
    for j in odd_walls:
        y,x = j
        if y ==0.0 and x!=0.0:
            y= -0.5
        if y !=0.0 and x==0.0:
            x= -0.5
        if y ==0.0 and x==0.0:
            y= -0.5
            x= -0.5
        right_odd_walls.append((y,x))
    #print(right_odd_walls)
    for j in even_walls:
        y,x = j
        if y ==(len(temp_pic_0[0])-1)/2 and x!=(len(temp_pic_0[0])-1)/2:
            y= (len(temp_pic_0[0])-1)/2+0.5
        if y !=(len(temp_pic_0[0])-1)/2 and x==(len(temp_pic_0[0])-1)/2:
            x= (len(temp_pic_0[0])-1)/2+0.5
        if y ==(len(temp_pic_0[0])-1)/2 and x==(len(temp_pic_0[0])-1)/2:
            y= (len(temp_pic_0[0])-1)/2+0.5
            x= (len(temp_pic_0[0])-1)/2+0.5
        right_even_walls.append((y,x))
    #print(right_even_walls)




    uierui_1 =[]
    for j in range(0,len(list_2)):
        wall_list =[]
        wall_list.append(list_2[j][0])
        wall_list.append(list_2[j][-1])
        uierui_1.append(wall_list)
    #print(uierui_1)

    use_walls =[]
    for j in range(0,len(uierui_1)):
        #print(uierui_1[j])
        for i in uierui_1[j]:
            y,x = i
            use_walls.append((x/2,y/2))
    #print(use_walls)
    odd_walls_2 =[]
    even_walls_2 =[]
    for x in range(0,len(use_walls)):
        if x %2 ==0:
            odd_walls_2.append(use_walls[x])
        else:
            even_walls_2.append(use_walls[x])
    #print(odd_walls_2)
    #print(even_walls_2)
    right_odd_walls_2 =[]
    right_even_walls_2 =[]
    for i in odd_walls_2:
        y,x =i
        if y ==0.0 and x!=0.0:
            y= -0.5
        if y !=0.0 and x==0.0:
            x= -0.5
        if y ==0.0 and x==0.0:
            y= -0.5
            x= -0.5
        right_odd_walls_2.append((y,x))
    #print(right_odd_walls_2)
    for j in even_walls_2:
        y,x = j
        if y ==(len(temp_pic_0)-1)/2 and x!=(len(temp_pic_0)-1)/2:
            y= (len(temp_pic_0)-1)/2+0.5
        if y !=(len(temp_pic_0)-1)/2 and x==(len(temp_pic_0)-1)/2:
            x= (len(temp_pic_0)-1)/2+0.5
        if y ==(len(temp_pic_0)-1)/2 and x==(len(temp_pic_0)-1)/2:
            y= (len(temp_pic_0)-1)/2+0.5
            x= (len(temp_pic_0)-1)/2+0.5
        right_even_walls_2.append((y,x))
    #print(right_even_walls_2)


    #for j in range(0,len(odd_walls)):





    return right_odd_walls,right_even_walls,right_odd_walls_2,right_even_walls_2
























def xxxx(a):
    final_xx_point =[]
    list_j = []
    for x in range(0,len(a),2):
        #print(a[x])
        for y in a[x]:
            j,i = y
            x1 = i / 2
            y1 = j / 2
            final_xx_point.append((x1,y1))
    #print(final_xx_point)
    d = sorted(final_xx_point , key=lambda k: [k[1], k[0]])
    #print(d)
    return d



pillar_1 =[]
pillar =[]
def size_of_largest_parallelogram(green_point_arry,ues_L):
    for j in range(0,len(green_point_arry)):
        for i in range(0,len(green_point_arry[j])):
            for x in all_the_x_number:
                j,i = x
                green_point_arry[j][i] =1
            for y in ues_L[0]:
                j,i = y
                green_point_arry[j][i] =1

    for j in range(0,len(green_point_arry)-1):
        for i in range(0,len(green_point_arry[j])-1):
            if green_point_arry[j][i] ==0:
                if green_point_arry[j-1][i] == 0 and green_point_arry[j+1][i] == 0 and green_point_arry[j][i+1] == 0 and green_point_arry[j][i-1] == 0\
                        and green_point_arry[j+1][i+1] ==0 and green_point_arry[j-1][i-1] ==0 and green_point_arry[j-1][i+1] == 0\
                    and green_point_arry[j+1][i-1] ==0:
                        pillar.append((j,i))
            if green_point_arry[0][0] == 0:
                if green_point_arry[0][1] ==0 and green_point_arry[1][0] ==0 and green_point_arry[1][1] ==0:
                    pillar.append((0,0))
            if green_point_arry[0][len(green_point_arry[j])-1] == 0:
                if green_point_arry[0][len(green_point_arry[j])-1-1] ==0 and green_point_arry[1][len(green_point_arry[j])-1] ==0 and green_point_arry[1][len(green_point_arry[j])-1-1] ==0:
                    pillar.append((0,len(green_point_arry[j])-1))
            if green_point_arry[-1][0] == 0:
                if green_point_arry[-2][0] == 0 and green_point_arry[-2][1] == 0 and green_point_arry[-1][1] == 0:
                    pillar.append((len(green_point_arry)-1,0))
            if green_point_arry[-1][-1] == 0:
                if green_point_arry[-1][-2] == 0 and  green_point_arry[-2][-1] == 0 and green_point_arry[-2][-2] == 0:
                    pillar.append((len(green_point_arry)-1,len(green_point_arry[j])-1))
            if green_point_arry[0][i] == 0:
                if green_point_arry[0][i-1] == 0 and green_point_arry[0][i+1] == 0 and green_point_arry[1][i] == 0\
                    and green_point_arry[1][i-1] == 0 and green_point_arry[1][i+1] == 0:
                    pillar.append((0,i))
            if green_point_arry[j][0] == 0:
                if green_point_arry[j][1] == 0 and green_point_arry[j-1][1] == 0 and green_point_arry[j+1][1] == 0\
                    and green_point_arry[j-1][0] == 0 and green_point_arry[j+1][0] == 0:
                    pillar.append((j,0))
            if green_point_arry[-1][i] == 0:
                if green_point_arry[-1][i-1]== 0 and green_point_arry[-1][i+1]== 0\
                    and green_point_arry[-2][i] == 0 and green_point_arry[-2][i-1] == 0 and green_point_arry[-2][i+1] == 0:
                    pillar.append((len(green_point_arry)-1,i))
            if green_point_arry[j][-1] == 0:
                if green_point_arry[j-1][-1] == 0 and green_point_arry[j+1][-1] == 0 and green_point_arry[j][-2] == 0\
                    and green_point_arry[j-1][-2] == 0 and green_point_arry[j+1][-2] == 0:
                    pillar.append((j,len(green_point_arry[j])-1))
    #print(list(set(pillar)))
    pillar_1 = sorted(set(pillar), key=pillar.index)
    return pillar_1









    '''
    [[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1], 
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1], 
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], 
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
     [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], 
     [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0]]

    
    '''








gates_point =[]
#gates
def gates(arry):
    gates = []
    L =[]
    gates_number =[]
    values =[]
    '''
    nb_of_shapes_ = colour_shapes_1(gates_arry)
    print(nb_of_shapes_)
    for value in nb_of_shapes_.values():
        values.append(value)
    '''



    for j in range(0,len(arry)):
        for i in range(0,len(arry[j])):
            if len(arry)== 3 and len(arry[j]) ==3 and arry[j][i] == 0:
                    gates.append((0,1))
                    gates.append((1,0))
                    gates.append((1,2))
                    gates.append((2,1))
            if len(arry)== 5 and len(arry[j])== 5:
                if arry[0][2] == 1 and arry[1][2] == 1 and arry[2][2] == 1 and arry[3][2] == 1 and arry[4][2] == 1:
                    gates.append((0,1))
                    gates.append((0,3))
                    gates.append((4,1))
                    gates.append((4,3))
                    gates.append((1,0))
                    gates.append((3,0))
                    gates.append((1,4))
                    gates.append((3,4))

    for i in range(0,len(arry[0])-4):
        if arry[0][i]==1 and arry[0][i+1] ==0 and arry[0][i+2] ==1:
            gates.append((0,i+1))
        if arry[0][i]==0 and arry[0][i+1] ==0 and arry[0][i+2] == 1:
            gates.append((0,i+1))
        if arry[0][i]==0 and arry[0][i-1] ==0 and arry[0][i+1] ==0 and arry[0][i+2] ==1:
            gates.append((0,i-1))
            gates.append((0,i+1))
        if arry[0][i]==0 and arry[0][i-1] ==0 and arry[0][i+1] ==0 and arry[0][i+2] ==0 and arry[0][i+3] ==0 :
            gates.append((0,i))
            gates.append((0,i+2))
        if len(arry[0]) == 5:
            if arry[0][i]==1 and arry[0][i+1]==0 and arry[0][i+2]==0 and arry[0][i+3]==0:
                gates.append((0,i+1))
                gates.append((0,i+3))
        if arry[0][-1] ==0 and arry[0][-2]==0 and arry[0][-3] == 1:
            gates.append((0,len(arry[0])-2))
    for i in range(len(arry[0])-1,0,-1):
        if arry[0][i]==0 and arry[0][i-1] ==1 and arry[0][i+1] ==1:
            gates.append((0,i))
    #print(gates)

    for i in range(0,len(arry[-1])-4):
        if arry[-1][i]==0 and arry[-1][i-1] ==1 and arry[-1][i+1] ==1:
            gates.append((len(arry)-1,i))
            #print(gates)
        if arry[-1][i]==0 and arry[-1][i-1] ==0 and arry[-1][i+1] ==1:
            gates.append((len(arry)-1,i))
            #print(gates)
        if arry[-1][i]==0 and arry[-1][i-1] ==0 and arry[-1][i+1] ==0 and arry[-1][i+2] ==1:
            gates.append((len(arry)-1,i-1))
            gates.append((len(arry)-1,i+1))
            #print(gates)
        if len(arry[-1])== 5:
            if arry[-1][i]==0 and arry[-1][i+1] ==0 and arry[-1][i+1] ==0 and arry[-1][i+2] ==0 and arry[-1][i+4] ==0:
                gates.append((len(arry)-1,i+1))
                gates.append((len(arry)-1,i+3))
        if arry[-1][-1] ==0 and arry[-1][-2]==0 and arry[-1][-3] == 1:
            gates.append((len(arry)-1,len(arry[-1])-2))
            #print(gates)

    for i in range(len(arry[-1])-2,0,-1):
        if arry[-1][i]==0 and arry[-1][i-1] ==1 and arry[-1][i+1] ==1:
            gates.append((len(arry)-1,i))
    #print(gates)




    for j in range(0,len(arry)-4):
        if arry[j][0] == 0 and arry[j-1][0] ==1 and arry[j+1][0] ==1:
            gates.append((j,0))
        if arry[j][0] == 0 and arry[j-1][0] ==0 and arry[j+1][0] ==1:
            gates.append((j,0))
        if arry[j][0] == 0 and arry[j+1][0] == 0 and arry[j+2][0] == 0 and arry[j+3][0] ==0 and arry[j+4][0] ==0:
            gates.append((j,0))
            gates.append((j+2,0))
            gates.append((j+4,0))
        if arry[j][0]==0 and arry[j-1][0] == 0 and arry[j+1][0] ==0 and arry[j+2][0] ==1:
            gates.append((j-1,0))
            gates.append((j+1,0))
        if arry[-1][0] ==0 and arry[-2][0]==0:
            gates.append((len(arry)-2,0))
    for j in range(len(arry)-2,0,-1):
        if arry[j][0]==0 and arry[j-1][0] ==1 and arry[j+1][0] ==1:
            gates.append((j,0))
    #print(gates)

    for j in range(0,len(arry)-4):
        if arry[j][-1] == 0 and arry[j-1][-1] ==1 and arry[j+1][-1] ==1:
            gates.append((j,len(arry[-1])-1))
            #print(gates)
        if arry[j][-1] == 0 and arry[j+1][-1] ==0 and arry[j+2][-1] == 0 and arry[j+3][-1] == 0 and arry[j+4][-1] ==1:
            gates.append((j+1,len(arry[-1])-1))
            gates.append((j+3,len(arry[-1])-1))
            #print(gates)
        if arry[j][-1] == 1 and arry[j+1][-1] ==0 and arry[j+2][-1] ==0 and arry[j+3][-1] ==1:
            gates.append((j+1,len(arry[-1])-1))
            #print(gates)
        if arry[j][-1]==0 and arry[j-1][-1] == 0 and arry[j+1][-1] ==0 and arry[j+2][-1] ==1:
            gates.append((j-1,len(arry[-1])-1))
            gates.append((j+1,len(arry[-1])-1))
        if arry[-1][-1] ==0 and arry[-2][-1]==0:
            gates.append((len(arry)-2,len(arry[-1])-1))
            #print(gates)
        if arry[-1][-1] ==0 and arry[-2][-1]==0 and arry[-3][-1]==0 and arry[-4][-1]==0:
            gates.append((len(arry)-4,len(arry[-1])-1))


    #print(gates)
    for x in gates:
        j,i = x
        if j<0 or i <0:
            L.append((j,i))
    #print(L)
    gates_1 =[]
    for x in gates:
        if x not in L:
            gates_1.append(x)
    #print(list(set(gates_1)))

    n = len(list(set(gates_1)))
    #print(gates)
    gates_point.append(list(set(gates_1)))
    if n == 0:
        return 'The maze has no gate.'
    if n ==1:
        return 'The maze has a single gate.'
    if n>1:
        return 'The maze has {} gates.'.format(n)

'''maze_2
   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22
0[[0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1], 
1 [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
2 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
3 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
4 [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
5 [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
6 [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
7 [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
8 [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0]]
'''












walls_point =[]
#walls
#深度搜索
def dfs(i,j,colour,arry): # 递归
    move_dict = { 'u': (-1, 0),'d': (1, 0), 'l': (0, -1),'r': (0, 1)}
    if j>=0 and j<len(arry) and i>=0 and i<len(arry[0]):
        if arry[j][i] == 1:
            arry[j][i] = colour
            for act in ['u','d','l','r']:
                yy = j + move_dict[act][0]
                xx = i + move_dict[act][1]
                dfs(xx, yy, colour,arry)

def colour_shapes(arry):#染色
    nb_of_shapes_ = defaultdict(list)
    colour = 2
    for j in range(0,len(arry)):
        for i in range(0,len(arry[j])):
            if arry[j][i] == 1:
                dfs(i,j,colour,arry)
                colour+=1
            if arry[j][i] > 1:
                nb_of_shapes_[arry[j][i]].append((j,i))
    #print(nb_of_shapes_)
    return nb_of_shapes_

def walls(arry):
    walls = []
    #walls_point =[]
    for i in colour_shapes(arry):
        walls.append(i)
        walls_point.append(colour_shapes(arry)[i])
    #print(walls_point)
    if len(walls) == 0:
        return 'The maze has no wall.'
    if max(walls) < 2:
        return 'The maze has no wall.'
    elif max(walls) == 2:
        return 'The maze has walls that are all connected.'
    elif max(walls) > 2:
        return 'The maze has {} sets of walls that are all connected.'.format(max(walls)-1)












L_inner_point =[]
#inner point
def dfs_inner_point(i,j,colour,inner_point_arry): # 递归
    move_dict = { 'u': (-1, 0),'d': (1, 0), 'l': (0, -1),'r': (0, 1)}
    if j>=0 and j<len(inner_point_arry) and i>=0 and i<len(inner_point_arry[0]):
        if inner_point_arry[j][i] == 0:
            inner_point_arry[j][i] = colour
            for act in ['u','d','l','r']:
                yy = j + move_dict[act][0]
                xx = i + move_dict[act][1]
                dfs_inner_point(xx, yy, colour,inner_point_arry)

def colour_shapes_1(inner_point_arry):#染色
    nb_of_shapes_ = defaultdict(list)
    colour = 2
    for j in range(0,len(inner_point_arry)):
        for i in range(0,len(inner_point_arry[j])):
            if inner_point_arry[j][i] == 0:
                dfs_inner_point(i,j,colour,inner_point_arry)
                colour+=1
            if inner_point_arry[j][i] > 1:
                nb_of_shapes_[inner_point_arry[j][i]].append((j,i))
    #print(nb_of_shapes_)
    return nb_of_shapes_

def ip(inner_point_arry):
    nb_of_shapes_ = colour_shapes_1(inner_point_arry)
    keys =[]
    values = []
    for value in nb_of_shapes_.values():
        values.append(value)
    #print(values)
    L_delete =[]
    for j in range(0,len(values)):
        for i in range(0,len(values[j])):
            y,x = values[j][i]
            if y == 0 or x == 0 or y == len(inner_point_arry)-1 or x ==len(inner_point_arry[0])-1:
                L_delete.append(values[j])
    #print(L_delete)
    temp = []
    for item in L_delete:
        if not item in temp:
            temp.append(item)
    L =[]
    #print(temp)
    for item in values:
        if item not in temp:
            L.append(item)
    #print(L)
    L_inner_point.append(L)
    #print(L_inner_point)
    a = 0
    for item in range(0,len(L)):
        if len(L[item]) ==1:
            a = a + 1
        if len(L[item]) != 1 and len(L[item]) % 2 != 0:
            a = a + (len(L[item])+1)//2
        if len(L[item]) % 2 == 0:
            a = a + len(L[item])//2
    #print(a)

    if a == 0:
        return 'The maze has no inaccessible inner point.'
    elif a == 1:
        return 'The maze has a unique inaccessible inner point.'
    elif a > 1:
        return 'The maze has {} inaccessible inner points.'.format(a)

















#accessible area.
def accessible_areas(accessible_areas_arry):
    L =[]
    nb_of_shapes_1 = colour_shapes_1(accessible_areas_arry)
    a = ip(accessible_areas_arry)
    #print(nb_of_shapes_1)
    #print(a)
    sL =[x for x in range(0,100000)]
    sl  =str(sL)
    b = ''
    for x in a:
        if x in sl:
            b = b + x
        if x not in sl:
            b = '0'
    #print(b)
    b = int(b)
    #print(b)
    for key in nb_of_shapes_1.keys():
        L.append(key)
    #print(L)

    nb_of_shapes_ = colour_shapes_1(accessible_areas_arry)
    values = []
    for value in nb_of_shapes_.values():
        values.append(value)
    #print(values)
    L_delete =[]
    for j in range(0,len(values)):
        for i in range(0,len(values[j])):
            y,x = values[j][i]
            if y == 0 or x == 0 or y == len(accessible_areas_arry)-1 or x ==len(accessible_areas_arry[0])-1:
                L_delete.append(values[j])
    #print(L_delete)
    temp = []
    for item in L_delete:
        if not item in temp:
            temp.append(item)
    L1 =[]
    #print(temp)
    for item in values:
        if item not in temp:
            L1.append(item)

    if len(L)-len(L1) == 0:
        return 'The maze has no accessible area.'
    if len(L)-len(L1) == 1:
        return 'The maze has a unique accessible area.'
    if len(L)-len(L1) > 1:
        return 'The maze has {} accessible areas.'.format(len(L)-len(L1))
















#cul_de_sac
def dfs_cul_de_sac(i,j,colour,cul_de_sac_arry): # 递归
    move_dict = { 'u': (-1, 0),'d': (1, 0), 'l': (0, -1),'r': (0, 1)}
    if j>=0 and j<len(cul_de_sac_arry) and i>=0 and i<len(cul_de_sac_arry[0]):
        if cul_de_sac_arry[j][i] == 0:
            cul_de_sac_arry[j][i] = colour
            for act in ['u','d','l','r']:
                yy = j + move_dict[act][0]
                xx = i + move_dict[act][1]
                dfs_cul_de_sac(xx, yy, colour,cul_de_sac_arry)

def colour_shapes_2(cul_de_sac_arry):#染色
    nb_of_shapes_ = defaultdict(list)
    colour = 2
    for j in range(0,len(cul_de_sac_arry)):
        for i in range(0,len(cul_de_sac_arry[j])):
            if cul_de_sac_arry[j][i] == 0:
                dfs_cul_de_sac(i,j,colour,cul_de_sac_arry)
                colour+=1
            if cul_de_sac_arry[j][i] > 1:
                nb_of_shapes_[cul_de_sac_arry[j][i]].append((j,i))
    #print(nb_of_shapes_)
    return nb_of_shapes_

L5 =[]
L6 = []
def spike(cul_de_sac_arry):
    nb_of_shapes_1 = colour_shapes_2(cul_de_sac_arry)
    #print(nb_of_shapes_1)
    number =[]
    for j in nb_of_shapes_1:
        for i in nb_of_shapes_1[j]:
            y,x =i
            count = 0
            for m, n in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_y = y + m
                new_x = x + n
                if 0<= new_y< len(cul_de_sac_arry) and 0<= new_x < len(cul_de_sac_arry[0]):
                    if cul_de_sac_arry[new_y][new_x] == cul_de_sac_arry[y][x]:
                        count = count + 1
            if count == 1:
                number.append((y,x))
    #print(number)
    L_delete =[]
    for j in number:
        y,x = j
        if  y == 0 or x ==0 or y == len(cul_de_sac_arry)-1 or x ==len(cul_de_sac_arry[0])-1:
            L_delete.append((y,x))
    #print(L_delete)
    tem =[]
    for x in number:
        if x not in L_delete:
            tem.append(x)
    #print(tem)

    #删内陆
    values = []
    for value in nb_of_shapes_1.values():
        values.append(value)
    #print(values)
    L_delete =[]
    for j in range(0,len(values)):
        for i in range(0,len(values[j])):
            y,x = values[j][i]
            if y == 0 or x == 0 or y == len(cul_de_sac_arry)-1 or x ==len(cul_de_sac_arry[0])-1:
                L_delete.append(values[j])
    #print(L_delete)
    temp = []
    for item in L_delete:
        if not item in temp:
            temp.append(item)
    L1 =[]
    #print(temp)
    for item in values:
        if item not in temp:
            L1.append(item)
    #print(L1)
    L2 =[]
    L3_1_1_1 =[]
    for j in range(0,len(L1)):
        for i in range(0,len(L1[j])):
            y,x = L1[j][i]
            L2.append((y,x))
    #print(L2)
    nb_of_shapes_22 = defaultdict(list)
    for x in tem:
        if x not in L2:
            L3_1_1_1.append(x)
    return L3_1_1_1

def change_pic(cul_de_sac_arry):
    L6 =[]
    L3_1_1_1 = spike(cul_de_sac_arry)
    L5.append(L3_1_1_1)
    for j in range(0,len(cul_de_sac_arry)):
        for i in range(0,len(cul_de_sac_arry[j])):
            for x in L3_1_1_1:
                j,i = x
                cul_de_sac_arry[j][i] = 1
        if len(L3_1_1_1) == 0:
            break
        else:
            change_pic(cul_de_sac_arry)
    L5_new = []
    for x in L5:
        if  x !=[]:
            L5_new.append(x)
    #print(L5_new)
    return (L5_new)

def gates_point_change_2(b,change_2_arry):
    L =[]
    for j in b:
        for i in j:
            y,x = i
            L.append((y,x))
    #print(L)
    for j in range(0,len(change_2_arry)):
        for i in range(0,len(change_2_arry[j])):
            for x in L:
                j,i = x
                change_2_arry[j][i] =1
    #print(change_2_arry)
    number =[]
    for j in range(0,len(change_2_arry)):
        for i in range(0,len(change_2_arry[j])):
            if change_2_arry[0][i] == 0:
                if change_2_arry[0][i-1] == 1 and change_2_arry[0][i+1] == 1 and change_2_arry[1][i] ==1:
                    number.append((0,i))
            if change_2_arry[-1][i] == 0:
                if change_2_arry[-1][i-1] == 1 and change_2_arry[-1][i+1] == 1 and change_2_arry[-2][i] ==1:
                    number.append((len(change_2_arry)-1,i))
            if change_2_arry[j][0] == 0:
                if change_2_arry[j-1][0] == 1 and change_2_arry[j+1][0] == 1 and change_2_arry[j][1] ==1:
                    number.append((j,0))
            if change_2_arry[j][-1] == 0:
                if change_2_arry[j-1][-1] == 1 and change_2_arry[j+1][-1] == 1 and change_2_arry[j][-1] ==1:
                    number.append((j,len(change_2_arry[j])-1))
    #print(list(set(number)))
    return list(set(number))












all_the_x_number = []
def change_2(a,c,new_Arry):

    #print(a)
    for j in a:
        for i in j:
            y,x = i
            all_the_x_number.append((y,x))
    #print(L)
    for x in c:
        j,i = x
        all_the_x_number.append((j,i))
    #print(L)
    for j in range(0,len(new_Arry)):
        for i in range(0,len(new_Arry[j])):
            for x in all_the_x_number:
                j,i = x
                new_Arry[j][i] =2

    #print(new_Arry)
    nb_of_shapes_ = colour_shapes_2_1(new_Arry)
    #print(nb_of_shapes_)
    n = len(nb_of_shapes_)
    #print(all_the_x_number)
    if n == 0:
        return 'The maze has no accessible cul-de-sac.'
    if n == 1:
        return 'The maze has accessible cul-de-sacs that are all connected.'
    if n >1:
        return 'The maze has {} sets of accessible cul-de-sacs that are all connected.'.format(n)

def dfs_inner_point_2(i,j,colour,inner_point_arry): # 递归
    move_dict = { 'u': (-1, 0),'d': (1, 0), 'l': (0, -1),'r': (0, 1)}
    if j>=0 and j<len(inner_point_arry) and i>=0 and i<len(inner_point_arry[0]):
        if inner_point_arry[j][i] == 2:
            inner_point_arry[j][i] = colour
            for act in ['u','d','l','r']:
                yy = j + move_dict[act][0]
                xx = i + move_dict[act][1]
                dfs_inner_point_2(xx, yy, colour,inner_point_arry)

def colour_shapes_2_1(cul_de_sac_arry):#染色
    nb_of_shapes_ = defaultdict(list)
    colour = 3
    for j in range(0,len(cul_de_sac_arry)):
        for i in range(0,len(cul_de_sac_arry[j])):
            if cul_de_sac_arry[j][i] == 2:
                dfs_inner_point_2(i,j,colour,cul_de_sac_arry)
                colour+=1
            if cul_de_sac_arry[j][i] > 1:
                nb_of_shapes_[cul_de_sac_arry[j][i]].append((j,i))
    #print(nb_of_shapes_)
    return nb_of_shapes_


'''
[[0, 0, 1, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1, 0, 0, 0, 1, 0, 1, 2, 1], 
 [0, 0, 1, 2, 1, 2, 1, 2, 2, 0, 1, 2, 2, 2, 1, 0, 0, 0, 1, 0, 1, 2, 1],
 [1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
 [1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1],
 [1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 3, 1], 
 [1, 2, 2, 2, 2, 2, 1, 3, 1, 0, 1, 0, 2, 2, 1, 2, 2, 0, 1, 3, 3, 3, 1],
 [1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 0, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
 [1, 0, 0, 0, 1, 2, 1, 2, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 1, 2, 1, 0, 0], 
 [1, 0, 0, 0, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1, 1, 2, 1, 0, 1, 2, 1, 0, 0]]

'''

all_1_pictre_use_for_xuxina =[]
use_L =[]
def entry_exit_paths(entry_exit_paths_arry):#l6 要改变
    L =[]
    L2 =[]
    temp_no_gates =[]
    delete_gates =[]
    for i in range(0,len(L_inner_point[0])):
        for j in L_inner_point[0][i]:
            #print(j)
            y,x =j
            L.append((y,x))
    use_L.append(L)
    #print(use_L)
    #print(gates_point)
    for x in range(0, len(gates_point[0])):
        L2.append(gates_point[0][x])
    #print(L2)

    for j in range(0,len(entry_exit_paths_arry)):
        for i in range(0,len(entry_exit_paths_arry[j])):
            if entry_exit_paths_arry[0][i] == 0:
                temp_no_gates.append((0,i))
            if entry_exit_paths_arry[-1][i] == 0:
                temp_no_gates.append((len(entry_exit_paths_arry)-1,i))
            if entry_exit_paths_arry[j][0] == 0:
                temp_no_gates.append((j,0))
            if entry_exit_paths_arry[j][-1] == 0:
                temp_no_gates.append((j,len(entry_exit_paths_arry[j])-1))
    #print(temp_no_gates)


    for x in temp_no_gates:
        if x not in L2:
            delete_gates.append(x)
    #print(list(set(delete_gates)))

    for j in range(0,len(entry_exit_paths_arry)):
        for i in range(0,len(entry_exit_paths_arry[j])):
            for x in all_the_x_number:
                j,i = x
                entry_exit_paths_arry[j][i] =1
            for y in L:
                j,i = y
                entry_exit_paths_arry[j][i] =1
            for z in list(set(delete_gates)):
                j,i = z
                entry_exit_paths_arry[j][i] =1
    #print(entry_exit_paths_arry)
    all_1_pictre_use_for_xuxina.append(entry_exit_paths_arry)

    nb_of_shapes_ = colour_shapes_2(entry_exit_paths_arry)
    #print(nb_of_shapes_)


    ture_pic = defaultdict(list)
    for j in nb_of_shapes_:
        for i in nb_of_shapes_[j]:
            #print(i)
            y,x = i
            for z in L2:
                y1,x2 = z
                if y ==y1 and x==x2:
                    ture_pic[j].append((x,y))
    #print(ture_pic)

    keys =[]
    tem =[]
    for key,value in ture_pic.items():
        keys.append(key)
        if len(value)>2:
            #print(key)
            tem.append(key)
    #print(tem)
    a = len(keys) - len(tem)
    if a ==0:
        return 'The maze has no entry-exit path with no intersection not to cul-de-sacs.'
    if a ==1:
        return 'The maze has a unique entry-exit path with no intersection not to cul-de-sacs.'
    if a >1:
        return 'The maze has {} entry-exit paths with no intersections not to cul-de-sacs.'.format(a)












































'''maze_2 xxx
[[0, 0, 1, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1, 0, 0, 0, 1, 0, 1, 2, 1], 
 [0, 0, 1, 2, 1, 2, 1, 2, 2, 0, 1, 2, 2, 2, 1, 0, 0, 0, 1, 0, 1, 2, 1],
 [1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
 [1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1],
 [1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 3, 1], 
 [1, 2, 2, 2, 2, 2, 1, 3, 1, 0, 1, 0, 2, 2, 1, 2, 2, 0, 1, 3, 3, 3, 1],
 [1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 0, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
 [1, 0, 0, 0, 1, 2, 1, 2, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 1, 2, 1, 0, 0], 
 [1, 0, 0, 0, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1, 1, 2, 1, 0, 1, 2, 1, 0, 0]]

'''



def how_display(A,pic_arry,green_point_arry,ues_L,a,find_wall_arry,all_1_pictre_use_for_xuxina):
    temp_wall =[]
    temp_wall_1 =[]
    lst2 =[]
    pillar_pillar_use =[]

    file = open(A[:-4]+'.tex','w')
    file.write("\\documentclass[10pt]{article}\n")
    file.write("\\usepackage{tikz}\n")
    file.write("\\pagestyle{empty}\n")
    file.write("\\usepackage[margin=0cm]{geometry}\n")
    file.write("\\tikzstyle{every node}=[cross out, draw, red]\n")
    file.write("\n")
    file.write("\\begin{document}\n")
    file.write("\n")
    file.write("\\vspace*{\\fill}\n")
    file.write("\\begin{center}\n")
    file.write("\\begin{tikzpicture}[scale = 0.5, x = 0.5cm, y = -0.25cm, thick, blue]\n")
    file.write("\\% Walls")

    #print(walls_point)
    for j in range(0,len(pic_arry)-2):
        for i in range(0,len(pic_arry[j])-2):
            if pic_arry[j][i] != 1 and pic_arry[j][i+1] == 1 and pic_arry[j][i+2] != 1:
                pass
               # print(j,i-1)

    #print(pillar)
    pillar_use = size_of_largest_parallelogram(green_point_arry,ues_L)
    #print(pillar_use)
    for x in pillar_use:
        j,i = x
        x1 = i //2
        y1 = j //2
        pillar_pillar_use.append((x1,y1))
    fd = sorted(pillar_pillar_use , key=lambda k: [k[1], k[0]])
    #print(fd)
    for x in fd:
        i,j = x
        x1 = i
        y1 = j
        print('    \\fill[green]  ({},{}) circle(0.2);'.format(x1,y1))
    print('% Inner points in accessible cul-de-sacs')
    # Inner points in accessible cul-de-sacs
    Inner_cul_de_sacs_use = xxxx(a)
    #print(Inner_cul_de_sacs_use)
    for x in Inner_cul_de_sacs_use:
        i,j = x
        x1 = i
        y1 = j
        print('    \\node at ({},{}) {};'.format(x1,y1,'{}'))


    list,list_2 = wall_find(find_wall_arry)
    #print(list)
    walls_list =[]
    uierui =[]
    for j in range(0,len(list)):
        walls_list =[]
        walls_list.append(list[j][0])
        walls_list.append(list[j][-1])
        uierui.append(walls_list)
    #print(uierui)
    use_walls =[]
    for j in range(0,len(uierui)):
        #print(uierui[j])
        for i in uierui[j]:
            y,x = i
            use_walls.append((x//2,y//2))
    #print(use_walls)
    odd_walls =[]
    even_walls =[]
    for x in range(0,len(use_walls)):
        if x %2 ==0:
            odd_walls.append(use_walls[x])
        else:
            even_walls.append(use_walls[x])
    #print(odd_walls)
    #print(even_walls)
    #for j in range(0,len(odd_walls)):

    for x in odd_walls:
        e =x
        e =str(x[0])
        f =str(x[1])
        #print(e)
        d = even_walls[odd_walls.index(x)]
        g =str(d[0])
        h =str(d[1])
        #print(g)
        print('    \draw ({},{}) -- ({},{});'.format(e,f,g,h))\


    #print(list_2)
    uierui_1 =[]
    for j in range(0,len(list_2)):
        wall_list =[]
        wall_list.append(list_2[j][0])
        wall_list.append(list_2[j][-1])
        uierui_1.append(wall_list)
    #print(uierui_1)

    use_walls =[]
    for j in range(0,len(uierui_1)):
        #print(uierui_1[j])
        for i in uierui_1[j]:
            y,x = i
            use_walls.append((x//2,y//2))
    #print(use_walls)
    odd_walls =[]
    even_walls =[]
    for x in range(0,len(use_walls)):
        if x %2 ==0:
            odd_walls.append(use_walls[x])
        else:
            even_walls.append(use_walls[x])
    #print(odd_walls)
    #print(even_walls)
    #for j in range(0,len(odd_walls)):

    for x in odd_walls:
        e =x
        e =str(x[0])
        f =str(x[1])
        #print(e)
        d = even_walls[odd_walls.index(x)]
        g =str(d[0])
        h =str(d[1])
        #print(g)
        #print('    \draw ({},{}) -- ({},{});'.format(e,f,g,h))

    i,j,k,l = Entry_exit_paths(all_1_pictre_use_for_xuxina)
    print(i)
    print(j)
    print(k)
    print(l)
    for x in i:
        e =x
        e =str(x[0])
        f =str(x[1])
        #print(e)
        d = j[i.index(x)]
        g =str(d[0])
        h =str(d[1])
        #print(g)
        print('    \draw[dashed, yellow] (({},{}) -- ({},{});'.format(e,f,g,h))
    for x in k:
        e =x
        e =str(x[0])
        f =str(x[1])
        #print(e)
        d = l[k.index(x)]
        g =str(d[0])
        h =str(d[1])
        #print(g)
        print('    \draw[dashed, yellow] (({},{}) -- ({},{});'.format(e,f,g,h))






















    file.write("\\end{tikzpicture}\n")
    file.write("\\end{center}\n")
    file.write("\\vspace*{\\fill}\n")
    file.write("\n")
    file.write("\\end{document}\n")
    file.close()


























pic_arry =[]
def analyse(will_use):
    arry=[]
    x_1_line =[]
    y_1_line =[]
    x_2_line =[]
    y_2_line =[]
    x_3_line =[]
    y_3_line =[]
    x_y_1_line = []
    x_y_2_line =[]
    x_y_3_line =[]

    for i in range(2*(len(will_use))-1):
        arry.append([0]*(2*len(will_use[0])-1))
    #print(arry)

    for j in range(0,len(will_use)):
        for i in range(0,len(will_use[j])):
            if will_use[j][i] == '1':
                x_1_line.append(j)
                y_1_line.append(i)
                x_y_1_line =list(zip(x_1_line,y_1_line))
            if will_use[j][i] =='2':
                x_2_line.append(j)
                y_2_line.append(i)
                x_y_2_line = list(zip(x_2_line,y_2_line))
            if will_use[j][i] =='3':
                x_3_line.append(j)
                y_3_line.append(i)
                x_y_3_line = list(zip(x_3_line,y_3_line))
    #print(x_y_1_line)
    #print(x_y_2_line)
    #print(x_y_3_line)

    for j in range(0,len(arry)):
        for i in range(0,len(arry[j])):
            for number in x_y_1_line:
                j_1,i_2 = number
                arry[2*j_1][2*i_2] = 1
                arry[2*j_1][2*i_2+1] = 1
                arry[2*j_1][2*i_2+2] = 1
            for number in x_y_2_line:
                j_1,i_2 = number
                arry[2*j_1][2*i_2] = 1
                arry[2*j_1+1][2*i_2] = 1
                arry[2*j_1+2][2*i_2] = 1
            for number in x_y_3_line:
                j_1,i_2 = number
                arry[2*j_1][2*i_2] = 1
                arry[2*j_1+1][2*i_2] = 1
                arry[2*j_1+2][2*i_2] = 1
                arry[2*j_1][2*i_2+1] = 1
                arry[2*j_1][2*i_2+2] = 1
    print(arry)

    inner_point_arry = copy.deepcopy(arry)
    accessible_areas_arry = copy.deepcopy(arry)
    cul_de_sac_arry = copy.deepcopy(arry)
    gates_arry = copy.deepcopy(arry)
    green_point_arry = copy.deepcopy(arry)
    new_Arry =copy.deepcopy(arry)
    change_2_arry =copy.deepcopy(arry)
    entry_exit_paths_arry = copy.deepcopy(arry)
    pic_arry = copy.deepcopy(arry)
    green_point_arry = copy.deepcopy(arry)
    find_wall_arry =copy.deepcopy(arry)

    id(inner_point_arry)
    id(accessible_areas_arry)
    id(cul_de_sac_arry)
    id(gates_arry)
    id(green_point_arry)
    id(new_Arry)

    print(gates(gates_arry))
    print(walls(arry))
    print(ip(inner_point_arry))
    print(accessible_areas(accessible_areas_arry))
    #print(spike(cul_de_sac_arry))
    #print(change_pic(cul_de_sac_arry))
    xiayiciyaoyong = change_pic(cul_de_sac_arry)
    #print(xiayiciyaoyong)
    b = copy.deepcopy(xiayiciyaoyong)
    a = copy.deepcopy(xiayiciyaoyong)
    #print(gates_point_change_2(b,change_2_arry))
    c = gates_point_change_2(b,change_2_arry)
    print(change_2(a,c,new_Arry))
    print(entry_exit_paths(entry_exit_paths_arry))
    #print(c)
    print(how_display(A,pic_arry,green_point_arry,use_L,a,find_wall_arry,all_1_pictre_use_for_xuxina))
    #print(size_of_largest_parallelogram(green_point_arry,use_L))
    #print(xxxx(a))
    print(Entry_exit_paths(all_1_pictre_use_for_xuxina))
    print(wall_find(find_wall_arry))


'''maze_1
[[1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
 [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
 [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1]]
'''
'''
[[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

'''








#begin
file = open('maze_1.txt','r')
A ='maze_2.txt'
will_use =[]
number_of_delete = ['\n']
exactly_number = ['0','1','2','3']
template = []

for line in file:
    line = line.replace(' ','')
    will_use.append(line)
    #print(will_use)
#delete \n
for j in range(0,len(will_use)):
    if will_use[j] not in number_of_delete:
        template.append(will_use[j])
will_use = template
#delete \n
for j in range(0,len(will_use)):
    for i in range(len(will_use[j])):
        if will_use[j][i]=='\n':
            will_use[j] = will_use[j].strip(will_use[j][i])
            will_use[j]= will_use[j]
            if will_use[j-1] == '':
                will_use.remove(will_use[j-1])
            if will_use[-1] == '':
                will_use.remove(will_use[-1])
#print(will_use)

for j in range(0,len(will_use)-1):
    if len(will_use[j])!=len(will_use[j+1]):
        print('Incorrect input')

#judge '0,1.2,3'
for j in range(0,len(will_use)):
    for i in range(len(will_use[j])):
        if will_use[j][i] not in exactly_number:
            print('Incorrect input')#change
        if len(will_use) < 2 or len(will_use[j]) < 2:
            print('Incorrect input')
        if len(will_use[j]) > 31 or len(will_use) > 41:
            print('Incorrect input')
        if will_use[j][-1] == '1' or will_use[j][-1] == '3':
            print('Input does not represent a maze')
        if will_use[-1][i] ==  '2' or will_use[-1][i] =='3':
            print('Input does not represent a maze')
#analyse



analyse(will_use)











