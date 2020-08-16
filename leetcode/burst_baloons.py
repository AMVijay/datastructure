class Solution:

    cached_score = {}
    
    def maxCoins(self, nums): 
        
        score = 0

        if tuple(nums) not in self.cached_score:
            score_matrix = []
            for index in range(len(nums)):
                # print("nums", nums)
                if index == 0 :
                    if len(nums) > 1: 
                        score_matrix.append(nums[index] * nums[index+1] + self.maxCoins(nums[:index]+nums[index+1:]))
                    else: 
                        # score_matrix[nums[index]] = nums[index] + self.maxCoins(nums[:index]+nums[index+1:])
                        score_matrix.append(nums[index])
                elif index == len(nums)-1:     
                    # score_matrix[nums[index]] = nums[index] * nums[index-1] + self.maxCoins(nums[:index]+nums[index+1:])
                    score_matrix.append(nums[index-1] * nums[index] + self.maxCoins(nums[:index]+nums[index+1:]))
                else:
                    # score_matrix[nums[index]] = nums[index-1] * nums[index] * nums[index+1] + self.maxCoins(nums[:index]+nums[index+1:])
                    score_matrix.append(nums[index-1] * nums[index] * nums[index+1] + self.maxCoins(nums[:index]+nums[index+1:]))
            # a1_sorted_keys = sorted(score_matrix, key=score_matrix.get, reverse=True)
            # for r in a1_sorted_keys:
                # print(r, score_matrix[r])
                # score = score_matrix[r]
                # break
            # if len(score_matrix) > 8:
            #     print(a1_sorted_keys)
            if len(score_matrix) > 0:    
                self.cached_score[tuple(nums)] = max(score_matrix)
            else: 
                self.cached_score[tuple(nums)] = 0
            # if len(self.cached_score) > 8:
            #     print("added to cached ::" , self.cached_score)

        return self.cached_score[tuple(nums)]


# input = [3,1,5,8]
# input = [9,76,64]
# input = [2,8,3,6,2,7,9]
# input = [9,76,64,21,97,60]
# input = [1,2,3,4,5]
# input = [35,16,83,87,84,59,48,41,20,54]
# input = [7,9,8,0,7,1,3,5,5]
input = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]
solution = Solution()
result = solution.maxCoins(input) 
print("Result Score :: ", result)