def Bubblesort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp

data=[5,1,4,2,8]
Bubblesort(data)
print(data)