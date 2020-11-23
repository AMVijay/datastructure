# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

# Complete the squares function below.
def squares(a, b):

    root_a = 1
    counter = 1
    while (root_a * 10) * (root_a * 10) < a: 
        root_a = root_a * 10
        counter = counter * 10
    # print("1 root_a, counter", root_a, counter)
    while counter > 10: 
        if (root_a + counter) * (root_a + counter) < a:
            root_a = root_a + counter   
        else: 
            counter = int(counter / 10)
    # print("2 root_a, counter", root_a, counter)
    while (root_a + 1) * (root_a + 1) <= a :
        root_a = root_a + 1

    if root_a * root_a != a:
        root_a = root_a + 1
    
    print("root_a", root_a)    

    root_b = 1
    counter = 1
    while (root_b * 10) * (root_b * 10) < b: 
        root_b = root_b * 10
        counter = counter * 10
    # print("1 root_a, counter", root_a, counter)
    while counter > 10: 
        if (root_b + counter) * (root_b + counter) < b:
            root_b = root_b + counter   
        else: 
            counter = int(counter / 10)
    # print("2 root_a, counter", root_a, counter)
    while (root_b + 1) * (root_b + 1) <= b:
        root_b = root_b + 1

    print("root_b", root_b)
    return root_b-root_a+1


a=3
b=9
print(a,b,squares(a,b))

a=17
b=24
print(a,b,squares(a,b))

a=24
b=49
print(a,b,squares(a,b))

a=100
b=1000
print(a,b,squares(a,b))

