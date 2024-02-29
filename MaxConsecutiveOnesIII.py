class MaxConsecutiveOnesIII:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if sum(nums)+k>=len(nums):
            return len(nums)

        start = end = 0
        counter = 0
        maxOnes = 0
        total = 0
        print ("start,end,total,counter")
        while end < len(nums):
            if ((counter < k) or (nums[end]==1)):
                counter += (1-nums[end])
                end += 1
                total += 1
            else:
                counter -= (1-nums[start])
                start += 1
                total -= 1
            if total > maxOnes: maxOnes = total

        return maxOnes