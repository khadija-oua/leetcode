class Solution(object):
    def reverseString(self, s):
        l=len(s)-1
        for r in range(len(s)/2):
            temp = s[r]
            s[r]=s[l]
            s[l]= temp
            l-=1
        return s
        