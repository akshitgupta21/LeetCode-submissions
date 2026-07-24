class Solution(object):
    def isAnagram(self, s, t):
        a=list(s)
        b=list(t)
        a.sort()
        b.sort()
        if a==b:
            return True
        else:
            return False
