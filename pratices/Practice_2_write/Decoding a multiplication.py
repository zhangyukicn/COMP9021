
def check_cloums_function(i,j):
    k = i * (j%10)
    for ii in list(str(k)):
        if len(list(str(k))) < 4:
            continue
    d = i*(int(j/10))
    for ii in list(str(k)):
        if len(list(str(d))) >= 4:
            continue
    total = k + d * 10
    for ii in list(str(total)):
        if len(list(str(total))) >= 5:
            continue
    the_Sum = i % 10 + j % 10 + k % 10 + total % 10
    if k // 1_000 + d // 100 + total // 1_000 == the_Sum\
            and i // 100 + k // 100 % 10 + d // 10 % 10 + total // 100 % 10 == the_Sum\
            and i // 10 % 10 + j // 10 + k // 10 % 10 + d % 10 + total // 10 % 10 == the_Sum:
        print(i // 10 % 10,j // 10,k // 10 % 10,d % 10,total // 10 % 10)
        return the_Sum

for x in range(0,1000):
    for y in range(0,100):
        if check_cloums_function(x,y):
             print('{} * {} = {}, all columns adding up to {}.'.format(x,y,x*y,check_cloums_function(x,y)))

'''
 411
  13
1233
411
5343

1+3+3+3
1
'''





































