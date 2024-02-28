class MaxKSumPairs:
    def maxOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        counter = {}
        for num in nums:
            if counter.get(k-num,0)>0:
                counter[k-num] -= 1
                answer += 1
            else:
                counter[num] = counter.get(num,0) + 1
        return answer