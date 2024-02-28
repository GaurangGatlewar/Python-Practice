class IncreasingTriplet:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minTable = [nums[0]]
        for i in range(1, len(nums)):
            minTable.append(min(minTable[-1],nums[i]))
        maxTable = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            maxTable.append(max(maxTable[-1],nums[i]))
        maxTable = maxTable[::-1]
        for i in range(1, len(nums)-1):
            if (minTable[i-1]<nums[i]) and (nums[i]<maxTable[i+1]):
                return True
        return False