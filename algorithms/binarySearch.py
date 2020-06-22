"""
-author = Vijay/am.vijay/Vijayaraaghavan Manoharan
"""

# Method to perform binary search
def binarysearch(searchElement,sortedList):
    midIndex = int(len(sortedList)/2)
    if(midIndex > 0):
        if(searchElement == sortedList[midIndex]):
            return searchElement
        else:
            if(searchElement<sortedList[midIndex]):
                sublist = sortedList[0:midIndex]
                return binarysearch(searchElement, sublist)
            else:
                sublist = sortedList[midIndex+1:len(sortedList)]
                return binarysearch(searchElement, sublist)
    elif(midIndex == 0 and searchElement == sortedList[midIndex]):
        return searchElement
    else:
        return Exception("Not Found")

# Test Case
datacollection = [1,2,3,4,5,6,7,8,9,10]
matchedElement = binarysearch(11,datacollection)
print("Matched Element value :: " + str(matchedElement))

