class Solution(object):
    def lengthOfLongestSubstring(self, s):
        M=0
        l=0
        k=set()
        for i in range(len(s)):
            if s[i] not in k : 
                k.add(s[i])
            else: 
                while s[i] in k :
                    k.remove(s[l])
                    l+=1
                k.add(s[i])
            
            M=max(M,len(k))
        return M
           
        