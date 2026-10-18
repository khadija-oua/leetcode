class Solution(object):
    def sortedSquares(self, nums):
        if not nums: return nums 
        if nums[0]>=0 : return [x**2 for x in nums]
        L=[]
        a=[]
        b=[]
        for n in nums:
            if n<=0 :a.append(n*(-1))
            else : b.append(n)
        i,j= 0,0
        k= len(a)-1
        while len(L)!=len(nums):
            if i <len(a) and j<len(b):
                if a[k-i]<=b[j]:
                    L.append(a[k-i])
                    i+=1
                else: 
                    L.append(b[j])
                    j+=1
                    
            elif i >=len(a) and j<len(b):
                L.append(b[j]) 
                j+=1
            elif j >=len(b) and i<len(a):
                L.append(a[k-i]) 
                i+=1
        return [x**2 for x in L]




        

