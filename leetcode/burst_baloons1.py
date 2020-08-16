class Solution:

    def partition_and_sort(self,nums,start_index, end_index):
        partition_value = nums[end_index]
        partition_value_index = end_index
        temp_index = start_index

        while temp_index <= end_index:
            if nums[temp_index] >= partition_value and temp_index < partition_value_index:
                temp = nums[temp_index]
                nums[partition_value_index] = temp
                nums[temp_index] = partition_value
                partition_value_index = temp_index
            elif nums[temp_index] < partition_value and temp_index > partition_value_index:
                temp = nums[temp_index] 
                nums[partition_value_index] = temp
                nums[temp_index] = partition_value
                partition_value_index = temp_index
            temp_index = temp_index + 1
        # print("partition_and_sort - end index, parition_index, partition_value :: " , end_index, partition_value_index, partition_value)
        return partition_value_index

    def quick_sort(self,nums,start_index, end_index):

        if start_index < end_index :
            partition_value_index = self.partition_and_sort(nums,start_index, end_index)
            if partition_value_index > 0 :
                self.quick_sort(nums, start_index, partition_value_index-1)
            self.quick_sort(nums, partition_value_index+1,end_index)


    def maxCoins(self, nums): 
        
        score = 0

        while len(nums) > 0 :

            if len(nums) == 1:
                score = score + nums[0]
                nums.pop(0)
            elif len(nums) == 2:
                score = score + (nums[0] * nums[1])
                minimum_value = min(nums[0], nums[1])
                print("mins number and index", minimum_value, nums.index(minimum_value))
                temp_index = nums.index(minimum_value)
                nums.pop(temp_index)
            else:
                if len(nums) > 3:
                    print("first parsing minimal nums reduce")
                    sorted_array = nums[1:len(nums)-1]
                    self.quick_sort(sorted_array,0, len(sorted_array)-1)
                    # remove the minimum value element lies in between big number
                    for element in sorted_array:
                        # print("element, nums", element, nums)
                        index = nums.index(element,1,len(nums)-1)
                        # print("index, element, nums", index, element, nums)
                        if index > 0 and index < len(nums)-1 and nums[index-1] > element and nums[index+1] > element:
                            score = score + (nums[index-1] * element * nums[index+1])
                            nums.pop(index)
                            print("score, nums", score, nums)
                while len(nums) > 2:
                    print("reduce the max combination number")
                    index = 0 
                    temp_score = 0 
                    for i in range(1, len(nums)-1):
                        print("reduce i ", i,temp_score,nums[i-1] * nums[i] * nums[i+1], index)
                        if (nums[i-1] * nums[i] * nums[i+1]) > temp_score:
                            index = i 
                            temp_score = nums[i-1] * nums[i] * nums[i+1]
                    score = score + (nums[index-1] * nums[index] * nums[index+1])
                    nums.pop(index)
                    print("score, nums, index", score, nums, index)
                
        return score


# input = [3,1,5,8]
# input = [9,76,64]
# input = [2,8,3,6,2,7,9]
# input = [9,76,64,21,97,60]
# input = [1,2,3,4,5]
# input = [9,76,64,21]
# input = [9,76,64,21,97,60,5]
input = [35,16,83,87,84,59,48,41,20,54]
solution = Solution()
result = solution.maxCoins(input) 
print("Result Score :: ", result)        