class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        maxSum=nums[0]
        for i in range(len(nums)):
            cur+=nums[i]
            maxSum=max(maxSum,cur)
            if cur<0:
                cur=0
        return maxSum