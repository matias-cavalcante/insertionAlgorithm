



def insertionAlg(array):
    keeper = 0
    holder = 0
    for num in range(1, len(array)):
        if num + 1 < len(array) and  array[num] > array[num+1]:
            keeper = array[num]
            array[num] = array[num+1]
            array[num+1] = keeper

        for val in range(0, num):
            i = (num+1) - (val+1)
            if i > 0 and array[i] < array[i-1]:
                holder = array[i-1]
                array[i-1] = array[i] 
                array[i]  = holder
    return array

#print(insertionAlg([17,6,1,4,3,9,2]))

#print(insertionAlg([8,2,1,2,7,9,5]))

print(insertionAlg([-2,2,0,3,1,4]))



