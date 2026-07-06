class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h={}
        for i in nums:
            if(i in h.keys()):
                return True
            else:
                h[i]=0
        return False        