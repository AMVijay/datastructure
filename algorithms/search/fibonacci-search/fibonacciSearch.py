"""
-author - am.vijay@gmail.com / Vijayaraaghavan Manoharan
"""

def fibonacciSearch(searchElement, sortedList):
    
    #fibonacci initial value
    fibonacciM2 = 0
    fibonacciM1 = 1
    fibonacciM = fibonacciM1 + fibonacciM2

    size = len(sortedList)
    
    # Find the first fibonacci value which is greater than size of the list.
    while (fibonacciM < size):
        fibonacciM2 = fibonacciM1
        fibonacciM1 = fibonacciM
        fibonacciM = fibonacciM1 + fibonacciM2
    
    print("Max fibonacci value ", fibonacciM)
    # Now going to reduce the max fibonacci value
    offset = -1
    while fibonacciM > 0:
        print("fibonnaci value : ",fibonacciM2,fibonacciM1, fibonacciM)
        index = min(offset+fibonacciM2,size-1)
        print("index value is ", index)
        if(index < size):
            # if search element is greater than the value at index derived then, 
            # shift the max fibonicci value left 1 value in its series.
            if(sortedList[index] < searchElement):
                fibonacciM =  fibonacciM1
                fibonacciM1 = fibonacciM2
                fibonacciM2 = fibonacciM - fibonacciM1
                offset = index
            # if search element is less than the value at index derived then,
            # shift the fibonicci value left 2 value in its series.
            elif(sortedList[index] > searchElement):
                fibonacciM = fibonacciM2
                fibonacciM1 = fibonacciM1 - fibonacciM2
                fibonacciM2 = fibonacciM - fibonacciM1
            # if search element is equal to the search element then return the index.
            elif(sortedList[index] == searchElement):
                return index

    return -1    

# Test Case
# datacollection = [1,2,3,4,5,6,7,8,9,10]

# matchedElementIndex = fibonacciSearch(3, datacollection)
# print("Element :: " + str(3) + " is at index :: " + str(matchedElementIndex))

# matchedElementIndex = fibonacciSearch(8, datacollection)
# print("Element :: " + str(8) + " is at index :: " + str(matchedElementIndex))

# matchedElementIndex = fibonacciSearch(6, datacollection)
# print("Element :: " + str(6) + " is at index :: " + str(matchedElementIndex))

# matchedElementIndex = fibonacciSearch(11, datacollection)
# print("Element :: " + str(11) + " is at index :: " + str(matchedElementIndex))


datacollection = [23,28,31,34,51,56,57,81,89,110]

matchedElementIndex = fibonacciSearch(81, datacollection)
print("Element :: " + str(81) + " is at index :: " + str(matchedElementIndex))
