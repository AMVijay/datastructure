class Solution:
    def maxSubArray(self, nums):
        start_index = 0
        end_index = 0
        sum = nums[0]
        for index in range(0, len(nums)):
            temp_sum = nums[0]
            for j in range(index, len(nums)):
                temp_sum = temp_sum + nums[j]
                if temp_sum > sum:
                    start_index = index
                    end_index = j
                    sum = temp_sum

        print("Sum", sum)
        print("start index :: {}, End Index :: {}", start_index, end_index)
        return sum

    def maxSubArray1(self, nums):
        sum = nums[0]
        length = len(nums)
        temp_sum = nums[0]
        index = 1
        while index < length:
            if temp_sum != None and nums[index] > temp_sum + nums[index]:
                temp_sum = nums[index]
            else:
                if temp_sum != None:
                    temp_sum = temp_sum + nums[index]
                else:
                    temp_sum = nums[index]

            if sum == None or temp_sum > sum:
                sum = temp_sum
            
            print(index,nums[index], sum)
            index = index + 1

        print("Sum", sum)
        return sum
         
    
solution = Solution()
# inputArray = [-2,1,-3,4,-1,2,1,-1]
inputArray = [1,2]
solution = solution.maxSubArray1(inputArray)
print(solution)
