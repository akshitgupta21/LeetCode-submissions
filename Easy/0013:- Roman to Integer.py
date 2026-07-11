class Solution(object):
    def ind(self,w):
        sum=0
        l=list(w)
        try:
            for b in range(len(l)):
                for a in range(len(l)):
                    if w[b]=="I":
                        if w[a]=="V":
                            c=a-b
                            if c == 1:
                                sum-=2                    
        except ValueError:
            pass
        try:
            for b in range(len(l)):
                for a in range(len(l)):
                    if w[b]=="I":
                        if w[a]=="X":
                            c=a-b
                            if c == 1:
                                sum-=2                 
        except ValueError:
            pass
        try:
            for b in range(len(l)):
                for a in range(len(l)):
                    if w[b]=="X":
                        if w[a]=="L":
                            c=a-b
                            if c == 1:
                                sum-=20                   
        except ValueError:
            pass
        try:
            for b in range(len(l)):
                for a in range(len(l)):
                    if w[b]=="X":
                        if w[a]=="C":
                            c=a-b
                            if c == 1:
                                sum-=20                    
        except ValueError:
            pass
        try:
            for b in range(len(l)):
                for a in range(len(l)):
                    if w[b]=="C":
                        if w[a]=="D":
                            c=a-b
                            if c == 1:
                                sum-=200                   
        except ValueError:
            pass
        try:
            for b in range(len(l)):
                for a in range(len(l)):
                    if w[b]=="C":
                        if w[a]=="M":
                            c=a-b
                            if c == 1:
                                sum-=200                    
        except ValueError:
            pass
        return sum 

    def romanToInt(self, s):
        a=list(s)
        b=a.count("I")
        i=b*1
        z=a.count("V")
        v=z*5
        e=a.count("X")
        x=e*10
        f=a.count("L")
        l=f*50
        g=a.count("C")
        c=g*100
        h=a.count("D")
        d=h*500
        j=a.count("M")
        m=j*1000
        o=self.ind(s)
        sum=i+v+x+l+c+d+m+o
        return sum

obj1=Solution()
obj1.romanToInt("III")
