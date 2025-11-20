class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars= [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        S=[]
        for p,s in cars : 
            S.append((target -p)/s)
            if len(S)>= 2 and  S[-1] <= S[-2] :
                S.pop()
        return len(S)