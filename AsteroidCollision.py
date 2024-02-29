class AsteroidCollision:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for asteroid in asteroids:
            st.append(asteroid)
            while len(st)>1:
                if st[-2]>0 and st[-1]<0:
                    asteroid1 = st.pop()
                    asteroid2 = st.pop()
                    if abs(asteroid1)>abs(asteroid2):
                        st.append(asteroid1)
                    elif abs(asteroid1)<abs(asteroid2):
                        st.append(asteroid2)
                    else:
                        continue
                else:
                    break
        return st