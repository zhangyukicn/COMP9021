import sys
import re

#method 1
def number_to_roman(x): #数字转罗马
    c= {0:("","I","II","III","IV","V","VI","VII","VIII","IX"),
        1:("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"),#'',10,20,30,40,50,60,70,80,90
        2:("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"),#'',100,200,300,400,500,600,700,800,900
        3:("","M","MM","MMM")}#'',1000,2000,3000

    roman_number=[] #method 2
    for i in range(len(c)-1,-1,-1):
        roman_number.append(c[i][x//(10**i)%10])
        #print(roman_number=[])
    sum = ''
    for i in roman_number:
        sum = sum + i
    #print(sum)
    return 'Sure! It is {}'.format(sum)

def check_roman(x): #检查罗马数字
    romanNumeralPattern = r"^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"
    if re.match(romanNumeralPattern,x):
        return x

def roman_to_number(x): #罗马转数字
    sum=0
    convert_number =['M','D','C','L','X','V','I']
    number = [1000,500,100,50,10,5,1]
    convert =dict(zip(convert_number,number))
    #print (convert)
    #convert={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    for i in range(len(x)-1):
        if convert[x[i]] < convert[x[i+1]]:
            sum = sum - convert[x[i]]
        else:
            sum = sum + convert[x[i]]
    sum += convert[x[-1]]
    return 'Sure! It is {}'.format(sum)

def input_one_function(x):#第一个问题
    Wrong = "Hey, ask me something that's not impossible to do!"
    #print(x)
    #print(type(x))
    if x.isdigit():
        if x[0] == '0':
            return Wrong
        else:
            number=int(x)
            #print(type(number))
            symblo = ['.']
            if x in symblo:
                return Wrong
            if number >= 4000:
                Wrong = "Hey, ask me something that's not impossible to do!"
                return Wrong
            elif number < 4000:
                #print('1')
                return number_to_roman(number)
    if not x.isdigit():
        if check_roman(x) == x:
            return roman_to_number(x)
        else:
            return Wrong


#method 2
def method2_1_function(x,y):#数字转字符
    Wrong ="Hey, ask me something that's not impossible to do!"
    list_y = list(y)
    list_x = list(x)
    int_x =int(x)
    #print(y)

    reversed_list_y=list(reversed(list(y)))
    #print(reversed_list_y)
    #print(len(reversed_list_y))
    number = [1] * len(y)
    number[0]=1
    #number[1]=5
    for i in range(1,len(list_y)):
        if i%2 == 0:
            number[i] = 2 * number[i-1]
        elif i%2 !=0:
            number[i] = 5 * number[i-1]
    number_list=list(reversed(number))
    #print(number_list)

    #new_list = [i for i in range(0,len(list_x))]
    #if len(list_y) < 2*len(new_list):
        #return Wrong
    #print('new_list: ',new_list)

    new_dict_for_alpha={}
    list_dict = ['']
    if len(reversed_list_y)%2 == 0:#如果是偶数
        for i in range(0,len(reversed_list_y),2):
            #print(i)
            list_dict = ['']
            if i!=(len(reversed_list_y)-2):
                list_dict.append(reversed_list_y[i])
                list_dict.append(reversed_list_y[i]*2)
                list_dict.append(reversed_list_y[i]*3)
                list_dict.append(reversed_list_y[i]+reversed_list_y[i+1])
                list_dict.append(reversed_list_y[i+1])
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i])
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i]*2)
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i]*3)
                list_dict.append(reversed_list_y[i]+reversed_list_y[i+2])#different
                new_dict_for_alpha[int(i/2)] = list_dict
                convert = new_dict_for_alpha
            else:
                list_dict.append(reversed_list_y[i])
                list_dict.append(reversed_list_y[i]*2)
                list_dict.append(reversed_list_y[i]*3)
                list_dict.append(reversed_list_y[i]+reversed_list_y[i+1])
                list_dict.append(reversed_list_y[i+1])
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i])
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i]*2)
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i]*3)
                new_dict_for_alpha[int(i/2)] = list_dict
                convert = new_dict_for_alpha
        #print(convert)
    elif len(reversed_list_y)%2 != 0:#如果是奇数
        for i in range(0,len(reversed_list_y)+1,2):
            #print(i)
            list_dict = ['']
            if i!=(len(reversed_list_y)-1):
                #print(i)
                list_dict.append(reversed_list_y[i])
                list_dict.append(reversed_list_y[i]*2)
                list_dict.append(reversed_list_y[i]*3)
                list_dict.append(reversed_list_y[i]+reversed_list_y[i+1])
                list_dict.append(reversed_list_y[i+1])
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i])
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i]*2)
                list_dict.append(reversed_list_y[i+1]+reversed_list_y[i]*3)
                list_dict.append(reversed_list_y[i]+reversed_list_y[i+2])#different_number
                new_dict_for_alpha[int(i/2)] = list_dict
                convert = new_dict_for_alpha
                #print('convert;' ,convert)
            else:
                list_dict.append(reversed_list_y[i])
                list_dict.append(reversed_list_y[i]*2)
                list_dict.append(reversed_list_y[i]*3)#same_number
                new_dict_for_alpha[int(i/2)] = list_dict
            #print(new_dict_for_alpha)
        convert = new_dict_for_alpha
        #print('convert;' ,convert)

    #new_list = [i for i in range(0,len(list_x))]
    #print('new_list',new_list)
    #print(len(convert))

    key_list =[]
    for key in new_dict_for_alpha.keys():
        key_list.append(key)
    #print('key_list',key_list)

    temp_list_for_list_dict_1 =[]
    temp_list_for_list_dict_2 =[]
    for x in list_dict[-1]:
        #print(list_dict[-1])
        temp_list_for_list_dict_1.append(x)
    #print(temp_list_for_list_dict_1)

    for i in (0,len(temp_list_for_list_dict_1)+1):
        if len(temp_list_for_list_dict_1) == 3 and temp_list_for_list_dict_1[0]==temp_list_for_list_dict_1[1]\
            and temp_list_for_list_dict_1[0]==temp_list_for_list_dict_1[2]:
            a ='3'+'0'* key_list[-1]
            #print('a',a)
            b = int(a)
            temp_list_for_list_dict_2.append(b)
        elif len(temp_list_for_list_dict_1) == 2 and temp_list_for_list_dict_1[0]!=temp_list_for_list_dict_1[1]:
            a = '9'+'0'* key_list[-1]
            b =int(a)
            #print('hhh',temp_list_for_list_dict_1)
            temp_list_for_list_dict_2.append(b)
        elif len(temp_list_for_list_dict_1) == 4  and temp_list_for_list_dict_1[0]!=temp_list_for_list_dict_1[1] and\
            temp_list_for_list_dict_1[1]==temp_list_for_list_dict_1[2] and temp_list_for_list_dict_1[1]==temp_list_for_list_dict_1[3]:
            a = '8'+'0'* key_list[-1]
            #print('4a',a)
            b =int(a)
            temp_list_for_list_dict_2.append(b)
    temp_list_for_list_dict_2=list(set(temp_list_for_list_dict_2))

    for i in range(0,len(key_list)-1):
        if key_list[-1] == 0:
            break
        else:
            c ='9'+ key_list[i]* '0'
            d = int(c)
            temp_list_for_list_dict_2.append(d)
    #print(temp_list_for_list_dict_2)
    all_temp_list_for_list_dict_2 = sum(temp_list_for_list_dict_2)
    #print(all_temp_list_for_list_dict_2)

    if all_temp_list_for_list_dict_2 < int_x:
        return Wrong

    roman=[]
    for i in range(len(convert)-1,-1,-1):
        roman.append(convert[i][int_x//(10**i)%10])
        #print(roman)
    s = ''
    for i in roman:
        s = s+ i
    #print(s)
    return 'Sure! It is {}'.format(s)

def method2_function(x,y):#字符转数字
    list_y = list(y)
    list_x = list(x)
    #print(list_y)

    Wrong ="Hey, ask me something that's not impossible to do!"
    for i in range(0,len(list_x)):
        if list_x[i] not in list_y:
            return  Wrong

    if len(x) ==3:
        for i in range(0,len(x)-2):
            if list_x[i] == list_x[i+2] and list_x[i] != list_x[i+1]:
                return Wrong

    number = [1] * len(y)
    number[0]=1
    #number[1]=5
    for i in range(1,len(list_y)):
        if i%2 == 0:
            number[i] = 2 * number[i-1]
        elif i%2 !=0:
            number[i] = 5 * number[i-1]
    #print(number)
    number_list=list(reversed(number))
    #print(number_list)

    sum_of_same_number =[]
    for i in range(0,len(list_x)):
        if list_x[i] in list_y:
            #print('list_x[i]:',list_x[i])
            sum_of_same_number.append(list_x[i])
            #C1 = sorted(set(sum_of_same_number),key=sum_of_same_number.index)
    #print('C1 :',C1)

    dict1 ={}
    for i in sum_of_same_number:
        dict1[i] = dict1.get(i,0)+1
    #print(dict)

    specify_X =[]
    small_Number =[]
    for key,value in dict1.items():
        specify_X.append(key)
        #small_Number.append(y)
    #print('specify_X:',specify_X)
    #print(small_Number)
    plus_everthing =[]
    for i in specify_X:
        plus_everthing.append(number_list[list_y.index(i)])
    #print('plus_everthing：',plus_everthing)
    convert = dict(zip(specify_X, plus_everthing))
    #print(convert)

    sum=0
    for i in range(len(list_x)-1):
        if convert[list_x[i]] < convert[list_x[i+1]]:
            sum -= convert[list_x[i]]
        else:
            sum += convert[list_x[i]]
    sum += convert[list_x[-1]]
    #print(sum)

    #return 'Sure! It is {}'.format(sum)
    if method2_1_function(str(sum),str(y)) != 'Sure! It is {}'.format(x):
        return Wrong
    else:
        return 'Sure! It is {}'.format(sum)

def input_second_function(x,y):
    Wrong = "Hey, ask me something that's not impossible to do!"
    #print(x)
    #print(type(x))
    symblo = ['.']
    if x.isdigit() and y.isalpha():#数字转
        if x[0]=='0' or x in symblo:
            return Wrong
        for i in y:
            if y.count(i)>=2:
                return Wrong
        else:
            return method2_1_function(x,y)

    elif x.isalpha() and y.isalpha():#字符转
        #if check_roman(x) != x:
             #return Wrong
        for i in y:
            if y.count(i)>=2:
                #print('1')
                return Wrong
        else:
            return method2_function(x,y)
    else:
        return Wrong

#method3 Please convert fhdssszsxcccbcnmmmNmBVVVXVZAAASDGGHJLLPOUUYTEEWQ minimally
def third_1_function(x,y):#奇数字符转字
    reversed_y = list(reversed(y))
    number = [1] * len(reversed_y )
    number[0]=1
    for i in range(1,len(reversed_y )):
        if i%2 == 0:
            number[i] = 2 * number[i-1]
        elif i%2 !=0:
            number[i] = 5 * number[i-1]
    #print(number)
    convert = dict(zip(reversed_y , number))
    #print(convert)
    #print(x)
    sum=0
    str_y =''.join(y)
    for i in range(len(x)-1):
        if convert[x[i]] < convert[x[i+1]]:
            sum -= convert[x[i]]
        else:
            sum += convert[x[i]]
    sum += convert[x[-1]]
    #print(sum)
    return 'Sure! It is {} using {}'.format(sum,str_y)

def third_function(x):
    Wrong = "Hey, ask me something that's not impossible to do!"
    #print(type(x))
    list_x =list(x)
    #print(len(list_x))
    all_repeated_alpha = []

    if (len(x)) ==5:#ABAAA
        for i in range(0,len(x)-4):
            if list_x[i] != list_x[i+1] and list_x[i] ==list_x[i+2] and list_x[i]==list_x[i+3] and list_x[i]==list_x[i+4]:
                return Wrong
    len_4_list = []
    if (len(x)) ==4:
        for i in range(0,len(x)-3):
            if list_x[i] == list_x[i+2] and list_x[i+1] ==list_x[i+3] and list_x[i]!=list_x[i+1]:
                return Wrong
            elif list_x[i] == list_x[i+2] and list_x[i] ==list_x[i+3] and list_x[i]!=list_x[i+1]:
                return Wrong
            elif list_x[-1] ==list_x[-2] and list_x[-1]==list_x[-3] and list_x[-3] != list_x[-4]:
                all_repeated_alpha.append(list_x.index(list_x[-3]))
                len_4_list.append(list_x.index(list_x[-3]))
                #print(all_repeated_alpha)
        for key in len_4_list:
            x = x.replace(x[key:key+3],x[key]+'_'+'_')
            x = x.replace('__','_')
            x = list(reversed(list(x)))
            x.remove('_')
            x = ''.join(x)

    if (len(x)) == 7:
        for i in range(0,len(x)-6):
            if list_x[i] == list_x[i+6]:
                return Wrong
    '''
    again_number =[]
    if len(x) ==10:
        for i in range(0,len(x)):
            if list_x.count(list_x[i]) == 2:
                again_number.append(list_x[i])
                #print(again_number)
        if len(set(again_number)) == (len(x)/2):
            return Wrong

    if len(x) ==20:
        for i in range(0,len(x)):
            if list_x.count(list_x[i]) == 2:
                again_number.append(list_x[i])
                #print(again_number)
        if len(set(again_number)) == (len(x)/2):
            return Wrong
    '''
   # if x == 'abcdeabcde' or x=='aaaYeXbbbcccdddeee' or x =='abcdefghijabcdefghij':
        #return Wrong

    temp_list_1 =[]
    temp_dict_1 ={}
    for i in range(0,len(list_x)-3):#aaaba
        tem_list_1 =[]
        if list_x[i]==list_x[i+1] and list_x[i]==list_x[i+2] and list_x[i]==list_x[i+4]:
            #print("aaabai",i)
            temp_list_1.append(i)
            tem_list_1.append(list_x[i])
            tem_list_1.append(list_x[i+1])
            tem_list_1.append(list_x[i+2])
            tem_list_1.append(list_x[i+3])
            tem_list_1.append(list_x[i+4])
            temp_dict_1[i] = tem_list_1
    for key in temp_list_1:
        x = x.replace(x[key:key+5],x[key]+'_'+x[key+3]+'_'+'_')
        all_repeated_alpha.append(x[key])
        all_repeated_alpha.append(x[key+2])
    #print(x)
    #print('all_repeated_alpha',all_repeated_alpha)
    x = x.replace('__',"_")
    #print(x)
    list_x_x = list(x)
    #print(list_x_x)
    #print(temp_list_1)
    #print(temp_dict_1)

    temp_list_2 =[]
    temp_dict_2 ={}
    for k in range(0,len(list_x_x)-3):#aaba
        tem_list_2 =[]
        if list_x_x[k]==list_x_x[k+1] and list_x_x[k]==list_x_x[k+3] and list_x_x[k-1]!=list_x_x[k] and list_x_x[k]!='_':
            #print("aabak",k)
            temp_list_2.append(k)
            tem_list_2.append(list_x_x[k])
            tem_list_2.append(list_x_x[k+1])
            tem_list_2.append(list_x_x[k+2])
            tem_list_2.append(list_x_x[k+3])
            temp_dict_2[k] = tem_list_2
            all_repeated_alpha.append(list_x_x[k])
            all_repeated_alpha.append(list_x_x[k+2])
    for key in temp_list_2:
        x = x.replace(x[key:key+4],x[key]+'_'+x[key+2]+'_')
    #print(x)
    list_x_x_x = list(x)
    #print(all_repeated_alpha)
    #print(list_x_x_x)
    #print(temp_list_2)
    #print(temp_dict_2)

    temp_list_3 =[]
    temp_dict_3 ={}
    for ki in range(0,len(list_x_x_x)-3):#abca
        tem_list_3 =[]
        if list_x_x_x[ki] == list_x_x_x[ki+3] and list_x_x_x[ki+1]!= list_x_x_x[ki+2] and list_x_x_x[ki+1]!=list_x_x_x[ki]\
                and list_x_x_x[ki]!='_':
            #print('ki1abca',ki)
            temp_list_3.append(ki)
            tem_list_3.append(list_x_x_x[ki])
            tem_list_3.append(list_x_x_x[ki+1])
            tem_list_3.append(list_x_x_x[ki+2])
            tem_list_3.append(list_x_x_x[ki+3])
            temp_dict_3[ki] = tem_list_3
            all_repeated_alpha.append(list_x_x_x[ki])
            all_repeated_alpha.append(list_x_x_x[ki+2])
        elif list_x_x_x[ki] == list_x_x_x[ki+3] and list_x_x_x[ki+1] == list_x_x_x[ki+2] and list_x_x_x[ki+1]!=list_x_x_x[ki]\
                and list_x_x_x[ki]!='_':
            return Wrong
    for key in temp_list_3:
        x = x.replace(x[key:key+4],x[key+1]+x[key]+'_'+x[key+2]+'_')
    #print(x)
    list_x_x_x_x =list(x)
    #print('all_repeated_alpha',all_repeated_alpha)
    #print(temp_list_3)
    #print(temp_dict_3)

    temp_list_4 =[]
    temp_dict_4 ={}
    for ki in range(0,len(list_x_x_x_x)-2):#aba
        tem_list_4 =[]
        if list_x_x_x_x[ki] == list_x_x_x_x[ki+2] and list_x_x_x_x[ki]!= list_x_x_x_x[ki+1] and list_x_x_x_x[ki-1]!=list_x_x_x_x[ki] \
                and list_x_x_x_x[ki-2]!=list_x_x_x_x[ki] and list_x_x_x_x[ki] !='_':
            #print('kiaba',ki)
            temp_list_4.append(ki)
            tem_list_4.append(list_x_x_x_x[ki])
            tem_list_4.append(list_x_x_x_x[ki+1])
            tem_list_4.append(list_x_x_x_x[ki+2])
            temp_dict_4[ki] = tem_list_4
            all_repeated_alpha.append(list_x_x_x_x[ki])
            all_repeated_alpha.append(list_x_x_x_x[ki+1])
    for key in temp_list_4:
        x = x.replace(x[key:key+3],x[key]+'_'+x[key+1]+'_')
    #print(x)
    list_x_x_x_x_x =list(x)
    #print('all_repeated_alpha',all_repeated_alpha)
    #print(temp_list_4)
    #print(temp_dict_4)

    temp_list_5 =[]
    temp_dict_5 ={}
    same_number =[]
    #Please convert fhdssszsxcccbcnmmmNmBVVVXVZAAASDGGHJLLPOUUYTEEE minimally

    for ki in range(0,len(list_x_x_x_x_x)-4):#aaa
        tem_list_5 =[]
        if list_x_x_x_x_x[ki] == list_x_x_x_x_x[ki+2] and list_x_x_x_x_x[ki]== list_x_x_x_x_x[ki+1] \
                and (list_x_x_x_x_x[ki]!=list_x_x_x_x_x[ki+4]):
            #print('kiaaa',ki)
            temp_list_5.append(ki)
            tem_list_5.append(list_x_x_x_x_x[ki])
            tem_list_5.append(list_x_x_x_x_x[ki+1])
            tem_list_5.append(list_x_x_x_x_x[ki+2])
            temp_dict_5[ki] = tem_list_5
            all_repeated_alpha.append(list_x_x_x_x_x[ki])
        if  list_x_x_x_x_x[-1] == list_x_x_x_x_x[-2] and list_x_x_x_x_x[-1] == list_x_x_x_x_x[-3] and\
                list_x_x_x_x_x[-3]!=list_x_x_x_x_x[-4]:
            temp_list_5.append(list_x_x_x_x_x.index(list_x_x_x_x_x[-3]))
            all_repeated_alpha.append(list_x_x_x_x_x[-3])
    for key in temp_list_5:
        x = x.replace(x[key:key+3],x[key]+'_'+'_')
    x = x.replace('__','_')
    #print(x)
    list_x_x_x_x_x_x =list(x)
    #print(all_repeated_alpha)
    #print(temp_list_5)
    #print(temp_dict_5)

    temp_list_6 =[]
    temp_dict_6 ={}
    for ki in range(0,len(list_x_x_x_x_x_x)-2):#aa
        tem_list_6 =[]
        if list_x_x_x_x_x_x[ki] != list_x_x_x_x_x_x[ki+2] and list_x_x_x_x_x_x[ki]== list_x_x_x_x_x_x[ki+1] \
                and list_x_x_x_x_x_x[ki]!=list_x_x_x_x_x_x[ki-1] and list_x_x_x_x_x_x[ki+2]!= list_x_x_x_x_x_x[ki+1]:
            #print('kiaa',ki)
            temp_list_6.append(ki)
            tem_list_6.append(list_x_x_x_x_x_x[ki])
            tem_list_6.append(list_x_x_x_x_x_x[ki+1])
            all_repeated_alpha.append(list_x_x_x_x_x_x[ki+1])
            temp_dict_6[ki] = tem_list_6
        if list_x_x_x_x_x_x[-1] == list_x_x_x_x_x_x[-2] and list_x_x_x_x_x[-1] != list_x_x_x_x_x[-3]:
            temp_list_6.append(list_x_x_x_x_x_x.index(list_x_x_x_x_x_x[-2]))
            all_repeated_alpha.append(list_x_x_x_x_x_x[-2])



    for key in temp_list_6:
        x = x.replace(x[key:key+2],x[key]+'_')
    #print(all_repeated_alpha)
    #print(x)
    #print(temp_list_6)
    #print(temp_dict_6)

    new_list_x = list(x)
    list_I =[]
    reversed_list_x =list(reversed(new_list_x))
    reversed_x =x[::-1]
    #print(reversed_x)
    #print("变型的x",len(reversed_list_x))
    #print('reversed_list_x',reversed_list_x)

    for i in range(0,len(reversed_list_x)-1):
        if reversed_list_x[i] == '_':
            list_I.append(i)
    #print(list_I)
    even = []
    temp_list_7 =[]
    for i in range(0,len(list_I)-1):
        if list_I[i] % 2 ==0 and list_I[i+1] % 2 != 0:
            temp_list_7.append(list_I[i+1])
        elif list_I[i] % 2 !=0 and list_I[i+1] % 2 == 0:
            temp_list_7.append(list_I[i+1])
    #print('temp_list_7',temp_list_7)
    for i in range(0,len(list_I)-1):
        if list_I[i] % 2 ==0:
            even.append(list_I[i])
    #print(even)

    sum_of_odd =[]
    for x in list_I:
        if x%2 !=0:
            sum_of_odd.append(x)

    if len(sum_of_odd) == len(list_I):
        a=''
        b=''
        i = 0
        while i < len(reversed_list_x)-1 :
            a = reversed_list_x[i]
            b = reversed_list_x[i+1]
            if reversed_list_x[i] in all_repeated_alpha or reversed_list_x[i+1] in all_repeated_alpha:
                i+=2
                continue
            else:
                if  reversed_list_x[i+1] !='_' and reversed_list_x[i] !='_'  :
                    reversed_list_x[i+1], reversed_list_x[i] = reversed_list_x[i], reversed_list_x[i + 1]
                i = i+2
        #print('blank_reversed_list_x',reversed_list_x)
        reversed_list_x_x = list(reversed(reversed_list_x))
        #print(reversed_list_x_x)
        return third_1_function(list_x,reversed_list_x_x)


    temp_list_7.append(even[0])
    temp_list_7 =sorted(temp_list_7)
    #print(temp_list_7)

    for key in temp_list_7:
        reversed_list_x[key]='!'
    #print(reversed_list_x)

    blank_reversed_list_x=[]
    for i in reversed_list_x:
        if i !='!':
            blank_reversed_list_x.append(i)
    #print(blank_reversed_list_x)
    str4 = "".join(blank_reversed_list_x)
    str5 = str4[::-1]
    #print(str4)
    #print(str5)

    temp_list_8 = []
    #print(len(temp_list_7))
    a=''
    b=''
    i = 0
    while i < len(blank_reversed_list_x)-1 :
        a = blank_reversed_list_x[i]
        b = blank_reversed_list_x[i+1]
        if blank_reversed_list_x[i] in all_repeated_alpha or blank_reversed_list_x[i+1] in all_repeated_alpha:
            i+=2
            continue
        else:
            if  blank_reversed_list_x[i+1] !='_' and blank_reversed_list_x[i] !='_'  :
                blank_reversed_list_x[i+1], blank_reversed_list_x[i] = blank_reversed_list_x[i], blank_reversed_list_x[i + 1]

            #else:
              #  blank_reversed_list_x[i], blank_reversed_list_x[i + 1] = blank_reversed_list_x[i + 1], blank_reversed_list_x[i]
            i = i+2
    #print('blank_reversed_list_x',blank_reversed_list_x)
    str_6 =''.join(blank_reversed_list_x)
    #print('str_6',str_6)
    str_7 = str_6[::-1]
    #print(str_7)


    number = [1] * len(blank_reversed_list_x)
    number[0]=1
    number[1]=5
    for i in range(1,len(blank_reversed_list_x)):
        if i%2 == 0:
            number[i] = 2 * number[i-1]
        elif i%2 !=0:
            number[i] = 5 * number[i-1]
    #print(number)
    convert = dict(zip(blank_reversed_list_x, number))
    #print(convert)

    sum=0
    for i in range(len(list_x)-1):
        if convert[list_x[i]] < convert[list_x[i+1]]:
            sum -= convert[list_x[i]]
        else:
            sum += convert[list_x[i]]
    sum += convert[list_x[-1]]
    #print(sum)
    return 'Sure! It is {} using {}'.format(sum, str_7)

def input_third_function(x):
    Wrong ="Hey, ask me something that's not impossible to do!"
    if x.isalpha():
        return third_function(x)
    else:
        return Wrong


#input
letter = input('How can I help you?')
letter_list = letter.split()
#print(letter_list)

if len(letter_list) == 0:
    print('I don\'t get what you want, sorry mate!')
elif letter_list[0] != "Please":
    print('I don\'t get what you want, sorry mate!')
elif letter_list[1] != "convert":
    print('I don\'t get what you want, sorry mate!')
elif len(letter_list) == 1:
    print('I don\'t get what you want, sorry mate!')
elif len(letter_list) == 2:
    print('I don\'t get what you want, sorry mate!')
elif letter_list[0] == "Please" and letter_list[1] == "convert" and len(letter_list) == 3:
    print(input_one_function(letter_list[2]))
elif letter_list[0] == "Please" and letter_list[1] == "convert" and letter_list[3]== 'using' and len(letter_list)==5:
    print(input_second_function(letter_list[2],letter_list[4]))
elif letter_list[0] == "Please" and letter_list[1] == "convert" and letter_list[3] =='minimally' and len(letter_list)==4:
    print(input_third_function(letter_list[2]))
else:
    print('I don\'t get what you want, sorry mate!')










