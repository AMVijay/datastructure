# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s, t, k):
    source_length = len(s)
    target_length = len(t)

    if (source_length + target_length) <= k:
            return "Yes"
    else:    
        max_index = source_length
        if source_length > target_length:
            max_index = target_length
        step_count = 0
        for index in range(max_index):
            if s[index] != t[index]:
                step_count = (source_length - index) + (target_length - index)
                break    

        index = index + 1
        if step_count == 0:
            if source_length > index:
                step_count = step_count + source_length - index
            if target_length > index:
                step_count = step_count + target_length - index 
            
        if step_count == k: 
            # print(step_count,k)
            return "Yes"
        elif step_count == 0 or step_count < k:
            # print(step_count, k, index)
            if k % 2 == 0: 
                if step_count % 2 == 0:
                    return "Yes"
                else:
                    return "No"
            else:
                if step_count % 2 == 1:
                    return "Yes"
                else: 
                    return "No"
        else: 
            return "No"


source = "hackerhappy"
target = "hackerrank"
k = 9
# Yes
print(source, target,k, appendAndDelete(source,target,k))

source = "a"
target = "z"
k = 7
# Yes
print(source, target,k, appendAndDelete(source,target,k))


source="abcd"
target="abcdert"
k=10
# No
print(source, target,k, appendAndDelete(source,target,k))

source="aaa"
target="a"
k=5
# Yes
print(source, target,k, appendAndDelete(source,target,k))

source="abcdef"
target="abcxyzr"
k=8
# No
print(source, target,k, appendAndDelete(source,target,k))


source="123456789"
target="1"
k=5
# No
print(source, target,k, appendAndDelete(source,target,k))

source="1"
target="101"
k=5
# Yes
print(source, target,k, appendAndDelete(source,target,k))

s = "123456789"
t = "1"
k = 5
# No
print(s, t,k, appendAndDelete(s,t,k))

s = "010101"
t = "01010"
k = 3
# Yes
print(s, t,k, appendAndDelete(s,t,k))

s="abc"
t="abc"
k=1
# No
print(s, t,k, appendAndDelete(s,t,k))

s="qwerasdf"
t="qwerzxcv"
k=8
# Yes
print(s,t,k,appendAndDelete(s,t,k))