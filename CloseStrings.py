class CloseStrings:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (len(word1) != len(word2)):
            return False

        if set(word1) != set(word2):
            return False

        counter1 = {}
        counter2 = {}
        for i in range(len(word1)):
            counter1[word1[i]] = counter1.get(word1[i],0) + 1
            counter2[word2[i]] = counter2.get(word2[i],0) + 1

        list1 = []
        for key in counter1:
            list1.append(counter1[key])
        list1.sort()
        list2 = []
        for key in counter2:
            list2.append(counter2[key])
        list2.sort()
        return (list1==list2)