class ContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left = 0
        right = len(height)-1
        while left < right:
            min_height = min(height[left], height[right])
            area = min_height*(right-left)
            if area > answer:
                answer = area
            if height[left] == min_height:
                left += 1
            else:
                right -= 1
        return answer