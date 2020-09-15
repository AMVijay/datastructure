def climbingLeaderboard(ranked, player):
    result = [] 
    uniqueScore = [] 
    previousValue = None
    rankCount = 1
    for element in ranked:
        if previousValue == None:
            uniqueScore.append(element)
        elif previousValue != element:
            uniqueScore.append(element)
        previousValue = element
    print(uniqueScore)
    length = len(uniqueScore)
    for element in player:
        if element >= uniqueScore[0]: 
            result.append(1)
        elif element == uniqueScore[length-1]:
            result.append(length)
        elif element < uniqueScore[length-1]:
            result.append(length+1)
        else:
            start_index = 0
            end_index = length
            mid_index = int(length/2)
            index_not_found = True
            while index_not_found == True:
                # if element == 65 :
                #     print("element ", element)
                #     print("mid index ", mid_index, uniqueScore[mid_index])
                #     print("start_index ", start_index)
                #     print("end index ", end_index)
                if element == uniqueScore[mid_index]:
                    result.append(mid_index+1)
                    index_not_found = False
                if end_index - start_index > 1:
                    if element < uniqueScore[mid_index] :
                        start_index = mid_index
                    else: 
                        end_index = mid_index
                    mid_index = int((start_index + end_index) / 2)
                else:
                    if element > uniqueScore[start_index]:
                        result.append(start_index+1)
                        index_not_found = False
                    else:
                        result.append(end_index+1)
                        index_not_found = False

    return result

# Test Case Data 1
ranked = [100,90,90,80,75,60]
player = [50,65,77,90,102]

# Test Case Data 2
# ranked = [100,100,50,40,40,20,10]
# player= [5,25,50,120]
result = climbingLeaderboard(ranked, player)
print("result : " , result)
