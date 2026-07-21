class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h=set()
        ans=[]
        for i in nums:
            if i in h:
                ans.append(i)
            else:
                h.add(i)
        return ans

         