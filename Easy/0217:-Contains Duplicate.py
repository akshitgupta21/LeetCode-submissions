class Solution(object):
    def containsDuplicate(self, nums):
        null_set=set()
        null_set.update(nums)
        if len(null_set)==len(nums):
            return False
        else:
            return True
