min_i = 10
max_i = 76
max_j = 87
max_k = 98
#set.union 交集
for i in range(min_i,max_i+1):
    i_digits = {i // 10, i % 10}
    if len(i_digits)!= 2:
        continue
    #print(i_digits)
    for j in range(i + 1, max_j + 1):
        j_digits = {j // 10, j % 10}
        if len(j_digits)!= 2:
            continue
        #print(j_digits)
        i_and_j_digits = i_digits.union(j_digits)
        if len(i_and_j_digits)!= 4:
            continue
        #print(i_and_j_digits)
        for k in range(j+1,max_k + 1):
            k_digits = {k // 10, k % 10}
            #print(k_digits)
            if len(k_digits) !=2:
                continue
            i_and_j_and_k_digits = i_and_j_digits.union(k_digits)
            #print(i_and_j_and_k_digits)
            if len(i_and_j_and_k_digits) !=6:
                continue
            #print(i_and_j_and_k_digits)
            product = i * j * k
            #print(product)
            if product >= 1_000_000:
                break
            if set(int(i) for i in str(product)) == i_and_j_and_k_digits:
                print(f'{i} x {j} x {k} = {product} is a solution.')
            for i in str(product)


