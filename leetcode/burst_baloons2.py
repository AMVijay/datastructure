class Solution:
    def maxCoins(self, nums) -> int:
            
            nums = [1]+nums+[1]
            size = len(nums)
            dp = [[0]*size for _ in range(size)]
            
            for i in range(size-1,-1,-1):
                for j in range(i+1,size):
                    for k in range(i+1,j):
                        score = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k])
                        if score == 1611297:
                            # print(dp)
                            print("dp[i][j], k", i, j, k, dp[i][j], dp[i][k], dp[k][j], nums[i], nums[j], nums[k], nums[i]*nums[j]*nums[k], dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k]) 
                        #max product for balloons between i and j
                        # choose a k to burst, max product for balloons b/w i,k + max product for balloons                     # between k,j
                        # now all the balloons in between are burst only i,k,j are left
                        # print("i,j,dp[i][j]",i,j,dp[i][j], nums[i], nums[j], nums[k], dp)
                        dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k])
                        
                        
            # print("created dp", dp)
            return dp[0][size-1]

# input = [35,16,83,87,84,59,48,41,20,54]
input = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]
solution = Solution()
result = solution.maxCoins(input) 
print("Result Score :: ", result)        