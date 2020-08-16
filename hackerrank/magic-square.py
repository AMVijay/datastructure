input = [[5,3,4],[1,5,8],[6,4,2]]

def magicSquare(s):
    changeCost = None

    possibleCombinations = []

    for i in range(1,4):
        for j in range(4,7):
            for k in range(7,10):
                if i != j and j != k and i != k and i + j + k == 15:
                    possibleCombinations.append([i,j,k])
                    possibleCombinations.append([i,k,j])
                    possibleCombinations.append([j,i,k])
                    possibleCombinations.append([j,k,i])
                    possibleCombinations.append([k,i,j])
                    possibleCombinations.append([k,j,i])
    
    possibleMagicSquares = []

    print(possibleCombinations)
    
    for row1 in possibleCombinations:
        for row2 in possibleCombinations:
            for row3 in possibleCombinations:
                if row1[0] not in row2 and row2[0] not in row3 and row1[0] not in row3: 
                    if row1[0] + row2[0] + row3[0] == 15 :
                        if row1[1] + row2[1] + row3[1] == 15 :
                            if row1[2] + row2[2] + row3[2] == 15 : 
                                if row1[0] + row2[1] + row3[2] == 15:
                                    if row1[2] + row2[1] + row3[0] == 15:
                                        possibleMagicSquares.append([row1,row2,row3])

    print(possibleMagicSquares)
    for magicSquare in possibleMagicSquares:
        tempCost = 0
        for i in range(3):
            for j in range(3):
                tempCost = tempCost + abs(magicSquare[i][j] - s[i][j])
        
        if changeCost == None or tempCost <= changeCost:
            changeCost = tempCost
            print("Change Cost and Magicsquare " , changeCost, magicSquare)

    return changeCost

result = magicSquare(input)
print(result)
