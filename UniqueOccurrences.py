class UniqueOccurrences:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = {}
        for num in arr:
            frequency[num] = frequency.get(num,0) + 1
        temp = []
        for key in frequency:
            temp.append(frequency[key])
        return (len(temp)==len(set(temp)))