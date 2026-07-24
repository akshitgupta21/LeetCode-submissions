class Solution(object):
    def removeElement(self, nums, val):
        k=0
        l=[]
        for i in range(len(nums)):
            if nums[i]==val:
                k+=1
                l.append(i)
        n=len(nums)-k
        if len(nums)==0:
            a=1
        else:
            a=max(nums)  
        for j in l:
            nums[j]=a+1
        nums.sort()                                       
                                                    
        return n
