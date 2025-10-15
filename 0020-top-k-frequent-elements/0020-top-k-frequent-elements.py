class Solution(object):
    def topKFrequent(self, nums, k):
        counter = {}
        for i in range(len(nums)):
            if nums[i] in counter :
                counter[nums[i]]+=1
            else :
                counter[nums[i]]=1
        sorted_count = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        
        return list(sorted_count.keys())[:k]