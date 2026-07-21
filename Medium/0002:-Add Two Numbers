class Solution(object):
    def __init__(self):
            self.head=None
    def addTwoNumbers(self, l1, l2):
        current=l1
        L1=[]
        while current!=None:
            a=current.val
            L1.append(a)
            current=current.next
        L2=[]
        curr=l2
        while curr!=None:
            b=curr.val
            L2.append(b)
            curr=curr.next
        L=[]     
        if len(L1)>=len(L2):   
            for i in range(len(L2)):
                a=L1[i]+L2[i]
                L.append(a)
            k=len(L1)-len(L2)
            m=len(L2)
            for i in range(m,m+k):
                L.append(L1[i])
            for i in range(len(L)):
                if L[i]>9:
                    try:
                        o=L[i]-10
                        L[i]=o
                        L[i+1]+=1 
                    except:
                        L.append(1)
        else:
            for i in range(len(L1)):
                a=L1[i]+L2[i]
                L.append(a)
                k=len(L2)-len(L1)
            m=len(L1)
            for i in range(m,m+k):
                L.append(L2[i])
            for i in range(len(L)):
                if L[i]>=10:
                    try:
                        o=L[i]-10
                        L[i]=o
                        L[i+1]+=1
                    except:
                        L.append(1)
        if len(L)==0:
            return self.head
        else: 
            head = None  
            for i in range(len(L)):
                new_node=ListNode(L[i])
                if head==None:
                    head=new_node
                else:
                    curr=head
                    while curr.next!=None:
                        curr=curr.next
                    curr.next=new_node
        return head








        
        
