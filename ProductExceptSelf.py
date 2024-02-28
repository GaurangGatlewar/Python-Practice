class ProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1 = [nums[0]]
        for i in range(1, len(nums)):
            nums1.append(nums1[-1]*nums[i])
        nums2 = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            nums2.append(nums2[-1]*nums[i])
        nums2 = nums2[::-1]
        answer = [nums2[1]]
        for i in range(1,len(nums)-1):
            answer.append(nums1[i-1]*nums2[i+1])
        answer.append(nums1[-2])
        return answer