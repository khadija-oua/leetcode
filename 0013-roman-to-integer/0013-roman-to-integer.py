class Solution(object):
    def romanToInt(self, s):
        sym = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0
        for i in range (len(s)-1) :
            if s[i]=="I" and ( s[i+1]=="V" or s[i+1]=="X"):
                res-=1
            elif s[i]=="X" and ( s[i+1]=="L" or s[i+1]=="C"):
                res-=10
            elif s[i]=="C" and ( s[i+1]=="D" or s[i+1]=="M"):
                res-=100
            else : 
                res += sym[s[i]]
        res += sym[s[-1]]
        return res 


         
       

        