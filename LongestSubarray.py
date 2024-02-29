class LongestSubarray:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == sum(nums): return len(nums)-1
        start = end = 0
        counter = 0
        maxOnes = 0
        total = 0
        while end < len(nums):
            if ((counter == 0) or (nums[end]==1)):
                total += nums[end]
                counter += (1-nums[end])
                end += 1
            else:
                total -= nums[start]
                counter -= (1-nums[start])
                start += 1
            if total > maxOnes: maxOnes = total
        return maxOnes