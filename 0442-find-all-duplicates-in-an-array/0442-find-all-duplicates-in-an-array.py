class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h = {}
        ans = []

        for i in nums:
            if (i in h):
                ans.append(i)
            else:
                h[i] = 1

        return ans