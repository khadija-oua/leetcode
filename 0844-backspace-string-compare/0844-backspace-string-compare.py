class Solution(object):
    def backspaceCompare(self, s, t):
        stacks =[]
        stackt=[]
        for c in s :
            if c == '#':
                if stacks : stacks.pop()
                else : continue
            else : 
                stacks.append(c)
        for c in t :
            if  c == '#':
                if stackt : stackt.pop()
                else : continue
            else : 
                stackt.append(c)
        return stackt == stacks
            

            
        


        