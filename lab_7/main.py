def Over_read():
    N = 0
    with open('input.txt', 'r') as f:
        for s in f:
            N += 1
    arr = []
    with open('input.txt', 'r') as f1:
        for s in f1:
            arr.append(s)
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    return arr
def After_read(arr):
    knot_link = [] #Массив связей
    
    # Формирование массива связей
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if int(arr[i][j]) >= 1:
                knot_link.append([i,j,int(arr[i][j])])
                
    #Очистка массива связей
    l = len(knot_link)
    for i in range(l):
        for j in range(l):
            if int(knot_link[i][0]) == int(knot_link[j][1]) and int(knot_link[i][1]) == int(knot_link[j][0]) and i != j:
                knot_link[i] = [0,0,0]
    l = len(knot_link)
    l1 = 0
    while True:
        if l1 >= len(knot_link):
            break
        if knot_link[l1] == [0,0,0]:
            knot_link.pop(l1)
        else:
            l1+=1
    return knot_link
def Prim_alg(arr):
    available = []
    end_arr = []

    available.append(int(0))
    for i in range(1,len(arr)):
        s_min = 1000000
        s_j = 0
        s_A = 0
        for A in available:
            for j in range(len(arr[A])):
                if int(arr[A][j]) != 0:
                    if j not in available and int(arr[A][j])<s_min:
                        s_j = j
                        s_A = int(A)
                        s_min = int(arr[A][j])
        available.append(s_j)
        end_arr.append([s_A,s_j,s_min])



    print(end_arr)



print('Минимальное оставное дерево: ',Kruskal_alg(After_read(Over_read())))
Prim_alg(Over_read())
