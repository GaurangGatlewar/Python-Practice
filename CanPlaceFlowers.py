class CanPlaceFlowers:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 0:
            return False

        if sum(flowerbed) + n > (len(flowerbed)+1)//2:
            return False

        flowerbed.append(0)
        flowerbed.insert(0,0)

        flowers = 0

        for i in range(1, len(flowerbed)-1):
            if (flowerbed[i-1]+flowerbed[i]+flowerbed[i+1])>0:
                continue
            flowerbed[i] = 1
            flowers += 1

        return (flowers>=n)