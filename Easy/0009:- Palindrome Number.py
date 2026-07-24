class Solution(object):
    def isPalindrome(self, x):
        l=[]
        d=str(x)
        for i in range(len(d)):
            l.append(d[i])
        a= l[:]
        l.reverse()
        if a==l:
            return True
        else:
            return False

c=Solution()
c.isPalindrome(121)
