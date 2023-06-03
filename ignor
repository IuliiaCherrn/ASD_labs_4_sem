import math
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
    
#Сложность Беллмана Форда  O(VE)
def alg_bellman_ford(src,arr):
    #print(After_read(arr))
    
    # Формирование массива связей
    knot_link = After_read(arr)
    #knot_link = [[0, 1, 5],[0, 2, 4],[1, 3, 3],[2, 1, 6],[3, 2, 2]]
    dist = [float("Inf")] * len(arr) #Массив растояний
    dist[src] = 0

    for i in range(len(arr) - 1):
        for s, d, w in knot_link:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                dist[d] = dist[s] + w

    for s, d, w in knot_link:
        if dist[s] != float("Inf") and dist[s] + w < dist[d]:
            print("Не допустим отрицательный вес пути")
            return
    return dist
print(alg_bellman_ford(len(Over_read())-1,Over_read()))
