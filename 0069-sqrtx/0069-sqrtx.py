class Solution(object):
    def mySqrt(self, x):
        s=1
        if x== 0: return 0
        while s <= x:
            if s*s == x :
                return s
            elif s*s > x:
                return s-1
            else : s+=1
        return s


        