#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def nonDivisibleSubset(k, s):

    mod_result = [[0 for i in range(len(s))] for j in range(len(s))]

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if (s[i] + s[j]) % k != 0:
                mod_result[i][j] = 1

    # print(mod_result)    
    result = []
    
    for i in range(len(s)):
        temp_result = []
        new_subarray = [i]
        temp_result.append(new_subarray)
        # print("temp_result size", len(temp_result))
        if len(result) < (len(s)-i) :
            for j in range(i+1,len(s)):
                if mod_result[i][j] == 1:
                    new_temp_result = []
                    for subarray in temp_result:
                        mod_check_condition_passed = True
                        # print("subarray", subarray)
                        for sub_array_index in range(len(subarray)):
                            if mod_result[subarray[sub_array_index]][j] == 0:
                                mod_check_condition_passed = False
                                new_subarray = subarray[:sub_array_index]
                                # print("new subarray", new_subarray)
                                new_subarray.append(j)
                                new_temp_result.append(new_subarray)
                                break
                        if mod_check_condition_passed == True:
                            subarray.append(j)
                    for new_subarray in new_temp_result:
                        if len(new_subarray) > 0:
                            temp_result.append(new_subarray)
        for subarray in temp_result:
            if len(result) < len(subarray):
                result = subarray
        
    print(result)
    return len(result)

def nonDivisibleSubset1(k, s):
    r, o = [0] * k, 0                            # 1
    result = []
    for i in s:
        r[i % k] += 1                            # 2
        if i%k in (8, 2,3,5):
            result.append(s.index(i))
    print(r)
    for j in range((k + 2) // 2):                # 3
        if not j or not k % 2 and j == k // 2:
            o += r[j] > 0
            print("r[j]", r[j])                        # 4
        else:
            print(j, k-j, r[j], r[k-j], max(r[j], r[k - j]))
            o += max(r[j], r[k - j])             # 5
    print(result)
    print(len(result))
    return(o)

if __name__ == '__main__':
    
    k = 7
    s = [576,496,727,410,124,338,149,209,702,282,718,771,575,436,278]

    # k = 2
    # s = [1,2,3,4,5,6]

    # k = 1
    # s = [3, 7, 2, 9, 1]

    # k=3
    # s = [1,4,9,3]

    # k=9
    # s=[61197933,56459859,319018589,271720536,358582070,849720202,481165658,675266245,541667092,615618805,129027583,755570852,437001718,86763458,791564527,163795318,981341013,516958303,592324531,611671866,157795445,718701842,773810960,72800260,281252802,404319361,757224413,682600363,606641861,986674925,176725535,256166138,827035972,124896145,37969090,136814243,274957936,980688849,293456190,141209943,346065260,550594766,132159011,491368651,3772767,131852400,633124868,148168785,339205816,705527969,551343090,824338597,241776176,286091680,919941899,728704934,37548669,513249437,888944501,239457900,977532594,140391002,260004333,911069927,586821751,113740158,370372870,97014913,28011421,489017248,492953261,73530695,27277034,570013262,81306939,519086053,993680429,599609256,639477062,677313848,950497430,672417749,266140123,601572332,273157042,777834449,123586826]

    result = nonDivisibleSubset(k, s)

    print(result)