
class Node:
    a_start_index = None
    b_end_index  = None
    palindrome_string = "-1"
    palindrome_string_length = None

    def __str__(self):
        return "palindrome string: %s, palindrome length %s, a_start_index %s, b_end_index %s" \
            %(self.palindrome_string, self.palindrome_string_length, self.a_start_index, self.b_end_index)

def isPalindrome(validate_string):
    is_palindrome = False
    if len(validate_string) > 1: 
        mid_index = int(len(validate_string)/2)
        mid_index_remainder = len(validate_string)%2
        # print(mid_index, mid_index_remainder, validate_string, validate_string[:mid_index],validate_string[mid_index+mid_index_remainder:])
        if validate_string[:mid_index] == validate_string[mid_index+mid_index_remainder:]:
            print("palindrome", validate_string, validate_string[:mid_index],validate_string[mid_index+mid_index_remainder:])
            isPalindrome = True
    return is_palindrome
#
# Complete the buildPalindrome function below.
#
def buildPalindrome(a, b):
    palindrome_nodes = []

    a_length = len(a)
    b_length = len(b)

    for index in range(a_length):
        palindrome_node = Node()
        palindrome_node.a_start_index = index

        for update_node in palindrome_nodes:
            print(index,a[update_node.a_start_index+1:index+1])
            if isPalindrome(a[update_node.a_start_index+1:index+1]) == True:
                update_node.palindrome_string = a[update_node.a_start_index+1:index+1]
                update_node.palindrome_string_length = len(update_node.palindrome_string)

        palindrome_nodes.append(palindrome_node)

    for node in palindrome_nodes:
        print(node.palindrome_string)

# a = "bac"
# b = "bac"

a = "abprstsyyyyqyyyys"
b = "pbat"

buildPalindrome(a,b)


