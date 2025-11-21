class Solution(object):
    def intersection(self, nums1, nums2):
        s = set()
        r=[]
        for n in nums1:
            if n not in s:
                s.add(n)
        for n in nums2:
            if n in s :
                r.append(n)
                s.remove(n)
        return r
