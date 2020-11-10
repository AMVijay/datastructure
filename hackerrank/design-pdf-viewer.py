# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    word_array = list(word)
    height = 0
    breadth = len(word_array)
    for character in word_array:
        temp_height = h[alphabets.find(character)]
        if  temp_height> height:
            height = temp_height

    return height * breadth

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
word = "zaba"
result = designerPdfViewer(h,word)
print(result)

