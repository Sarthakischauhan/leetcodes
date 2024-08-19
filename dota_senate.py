class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr,qd = [], []
        for i in range(len(senate)):
            if (senate[i] == "R"):
                qr.append(i)
            else:
                qd.append(i)
        
        while qr and qd:
            if (qr[0] < qd[0]):
                qr.append(qr.pop(0) + len(senate))
                qd.pop(0)
            else:
                qd.append(qd.pop(0) + len(senate))
                qr.pop(0)
        return "Radiant" if qr else "Dire"
