def bubbleSort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]


l = [3,7,8,4,1,6,5,2,9]
bubbleSort(l)
print(l)