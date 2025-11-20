class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for n in s:
            if n.isalnum():
               a+=n.lower()
        right = len(a)-1
        for left in range(len(a)):
            if a[left] == a[right]:
                right-=1
            else:
                return False 
        return True