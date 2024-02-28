class ProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]
        for i in range(len(nums)-1):
            product.append(product[-1]*nums[i])
        multiplier = 1
        for i in range(len(nums)-1,0,-1):
            multiplier *= nums[i]
            product[i-1] *= multiplier
        return product