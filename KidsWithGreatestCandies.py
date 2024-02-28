class KidsWithGreatestCandies:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        limit = max(candies)-extraCandies
        return [candy>=limit for candy in candies]