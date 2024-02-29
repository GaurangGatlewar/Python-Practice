class LargestAltitude:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = altitude = 0
        for num in gain:
            altitude += num
            maxAltitude = max(altitude,maxAltitude)
        return maxAltitude