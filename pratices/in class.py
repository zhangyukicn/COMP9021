L,M = input('give me two word:').split()#用spilt里什么样子的分隔符分开
print(L)
print(M)

while True:
    try:
        numbers = int(input('give me a nuber'))
        print('ok, I rember')
        break
    except ValueError:
        print('game mistake')

print('Yes, By All Means, Yes!'.istitle())
