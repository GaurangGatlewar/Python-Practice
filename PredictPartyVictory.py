class PredictPartyVictory:
    def predictPartyVictory(self, senate: str) -> str:

        senate = list(senate)
        counter = 0
        while len(set(senate))>1:
            senator = senate.pop(0)
            if ((counter>=0) and (senator=='D')):
                senate.append(senator)
            elif ((counter<=0) and (senator=='R')):
                senate.append(senator)
            else:
                pass
            counter += (senator=='D') - (senator=='R')

        if senate[0] == 'D':
            return "Dire"
        else:
            return "Radiant"