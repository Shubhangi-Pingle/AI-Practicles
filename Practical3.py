size=int(input("\nEnter the size of the array"))

def getArray():
    for i in range(0,size):
        array.append(int(input("\nEnter the Element: ")))


def selection_sort():
    for i in range(0,size-1):
        min_index=i
        for j in range(i+1,size):
            if array[min_index]>array[j]:
                min_index=j
        # temp=array[i]
        # array[i]=array[min_index]
        # array[min_index]=temp
        array[i],array[min_index]=array[min_index],array[i]
        print("Iteration:",i+1,array)



while True:
    ch=int(input("\nENter your choice:"))
    if ch==1:
        array=[]
        getArray()
        selection_sort()
    else:
        print("\nInvalid Choice!")
        break



 