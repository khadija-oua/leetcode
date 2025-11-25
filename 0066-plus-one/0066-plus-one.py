class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        R=[]
        d=1
        for i in range(len(digits)):
            d += digits[i]*(10**(len(digits)-i-1))
        for n in str(d):
            R.append(int(n))
        return R

        