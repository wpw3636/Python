class Solution:
    def runningSum(self, nums):
        runningsum = []
        num = 0
        for n in nums:
            num += n
            runningsum.append(num)
        return runningsum  
    
nums = [1,2,3,4]
sol = Solution()
print(sol.runningSum(nums))