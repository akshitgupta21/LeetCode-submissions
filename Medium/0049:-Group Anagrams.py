class Solution(object):
    def groupAnagrams(self, strs):
        l=[]
        list1=[]
        for i in range(len(strs)):
            d=strs[i]
            s=list(d)
            s.sort()
            a="".join(s)
            l.append(a)
        set1=set(l)
        for j in set1:
            a=0
            c=[]
            for k in range(len(l)):
                if l[k]==j:
                    c.append(strs[k])
                    a+=1
            list1.append(c)
        return list1
