class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[i])
        for j in range(len(nums)):
            ans.append(nums[j])
        return ans
