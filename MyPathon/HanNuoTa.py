
def initArray(n):
    array = []
    for i in range(n+1):
        if i==0:
            continue
        array.append(i)
    array.reverse()
    print(array)
    return array

array1=initArray(3)
array2=initArray(0)
array3=initArray(0)
def moven(n,array1,array2,array3):
    if n==1:
        move(array1, array3)
        print(array1, array2, array3)
    else:
        moven(n-1, array1, array3, array2)
        moven(1, array1, array2, array3)
        moven(n-1, array2, array1, array3)

def move(array1,array2):
    if not array1:
        return False
    if  array2 and array1[len(array1)-1] > array2[len(array2)-1]:
        return False
    array2.append(array1.pop())
    return True
print(array1,array2,array3)
moven(3,array1,array2,array3)




