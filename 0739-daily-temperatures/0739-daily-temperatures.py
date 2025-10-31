class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        answer =[0]*n
        stack =[] #pair of tempt and index
        for i,t in enumerate(temperatures):
            while stack and t >stack[-1][0]:
                stackt ,stackInd = stack.pop()
                answer[stackInd] = (i - stackInd)
            stack.append([t,i])
        return answer

            

        