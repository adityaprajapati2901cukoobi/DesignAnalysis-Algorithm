def mergeSort(array):
    if len(array)>1:
        r=len(array)//2
        l=array[:r]
        u=array[r:]
        mergeSort(l)
        mergeSort(u)
        i=0
        j=0
        k=0

        while i<len(l) and j<len(u):
            if l[i] < u[j]:
                array[k]=l[i]
                i+=1
            else:
                array[k]=u[j]
                j+=1
            k+=1

        while i<len(l):
            array[k]=l[i]
            i+=1
            k+=1

        while j<len(u):
            array[k]=u[j]
            j+=1
            k+=1
   
def printList(array):
    for i in range(len(array)):
        print(array[i]," ")
    print()

if __name__ =='__main__':
    array=[2,3,5,6,1,3,5,3]

    mergeSort(array)
    printList(array)