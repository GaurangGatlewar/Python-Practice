class MaximumAverageSubarrayI:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k>=len(nums):
            return sum(nums)/k

        currSum = maxSum = sum(nums[:k])
        for i in range(len(nums)-k):
            currSum += nums[i+k]-nums[i]
            if currSum>maxSum: maxSum = currSum
        return (maxSum/k)