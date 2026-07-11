class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    return l
a=Solution()
a.twoSum([2,7,11,15],9)
