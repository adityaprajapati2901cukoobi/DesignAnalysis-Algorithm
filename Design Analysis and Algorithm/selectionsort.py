def selectionSort(array):
    for step in range(size):
        minn=step
        for i in range(step+1,size):
            if array[i]<array[minn]:
                minn=i

        (array[step],array[minn])=(array[minn],array[step])

array=[1,2,15,2,31,56,23,1]
size=len(array)
selectionSort(array,size)
print(array)

