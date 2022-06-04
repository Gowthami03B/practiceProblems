def insertionSort(array):
    #nums = [9,5,4,1,3]
    for step in range(1, len(array)):
        key = array[step] #in first step second element is key
        j = step - 1 #j is always step - 1 to continue next iteration
           
        while j >= 0 and key < array[j]: #since j is step - 1, check if key(2nd ele) is < arr[j]
            #if so, we swap all elements to next position
            array[j + 1] = array[j]
            j = j - 1#dec j
        
        array[j + 1] = key #the j + 1th position is the new insertion and correct position for element
    return nums


nums = [9,5,4,1,3]
print(insertionSort(nums))


        
