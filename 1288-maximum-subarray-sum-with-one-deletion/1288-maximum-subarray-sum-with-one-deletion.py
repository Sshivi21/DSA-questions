class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maxSum=arr[0]
        mw=0
        mwo=arr[0]
        for i in range(1,len(arr)):
            mw=max(mwo,mw+arr[i])
            mwo=max(mwo+arr[i],arr[i])
            maxSum=max(maxSum,mw,mwo)
        return maxSum