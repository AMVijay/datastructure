"""
-author = Vijay/am.vijay/Vijayaraaghavan Manoharan
"""
# Method to perform binary search
def binarySearch(searchElement, startIndex, endIndex, sortedList):
    # print("Mid Index :: " + str(midIndex))
    if(endIndex > startIndex):
        midIndex = int((endIndex + startIndex) / 2)
        if(searchElement == sortedList[midIndex]):
            return midIndex
        else:
            if(searchElement<sortedList[midIndex]):
                return binarySearch(searchElement, startIndex,midIndex-1,sortedList)
            else:
                return binarySearch(searchElement, midIndex+1, endIndex, sortedList)
    elif(startIndex == endIndex and searchElement == sortedList[startIndex]):
        return startIndex
    else:
        return Exception("Not Found")

# Test Case
datacollection = [1,2,3,4,5,6,7,8,9,10]

matchedElementIndex = binarySearch(3,0, len(datacollection)-1, datacollection)
print("Element :: " + str(3) + " is at index :: " + str(matchedElementIndex))

matchedElementIndex = binarySearch(8,0, len(datacollection)-1, datacollection)
print("Element :: " + str(8) + " is at index :: " + str(matchedElementIndex))

matchedElementIndex = binarySearch(6,0, len(datacollection)-1, datacollection)
print("Element :: " + str(6) + " is at index :: " + str(matchedElementIndex))

matchedElementIndex = binarySearch(11,0,len(datacollection)-1,datacollection)
print("Element :: " + str(11) + " is at index :: " + str(matchedElementIndex))

