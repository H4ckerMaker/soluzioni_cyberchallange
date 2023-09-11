def build_combination(lista):
    list = lista[::-1]
    max_list = [list[0]]
    for count, num in enumerate(list):
        if num > max_list[0]:
            max_list.insert(0, num)
        else:
            rel_list = [num]
            #--------relative list sbagliata---------- 
            for n in list[::-1][len(list) - count :]:
                if n < rel_list[-1]:
                    rel_list.append(n)
            #-----------------------------------------
            print(count, num, rel_list, max_list)
            if sum(rel_list) > sum(max_list):
                max_list = rel_list
            print(count, max_list)
    return max_list

with open('../input/input4.txt') as f:
    N = int(f.readline())
    T = f.readline().strip().split(' ')

W = [int(w) for w in T]
print(W)
print(build_combination(W))
