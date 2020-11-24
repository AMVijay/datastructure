# https://www.hackerrank.com/challenges/repeated-string/problem?h_r=profile

# Complete the repeatedString function below.
def repeatedString(s, n):

    number_of_sets = 1
    last_set_length = n
    string_length = len(s)
    
    if n > string_length:
        number_of_sets = n // string_length
        last_set_length = n % string_length
    
    a_count = 0
    last_set_a_count = 0
    max_index = string_length
    if number_of_sets == 1: 
        max_index = last_set_length
    for i in range(max_index):
        if s[i] == 'a': 
            a_count = a_count + 1
            if i < last_set_length:
                last_set_a_count = last_set_a_count + 1
        
    if number_of_sets > 1:
        a_count = a_count * number_of_sets + last_set_a_count

    return a_count

s = "a"
n = 10000000000000
print(s,n, repeatedString(s,n))

s = "aba"
n = 10
print(s,n, repeatedString(s,n))