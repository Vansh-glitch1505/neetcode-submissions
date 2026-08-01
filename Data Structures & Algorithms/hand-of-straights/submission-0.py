class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = {}
        if len(hand) % groupSize != 0:
            return False
        
        for i in range(len(hand)):
            freq[hand[i]] = 1 + freq.get(hand[i], 0)
        
        for card in hand:
            if freq[card] == 0:
                continue
            
            for nxt in range(card, card + groupSize):
                if freq.get(nxt, 0) == 0:
                    return False
                freq[nxt] -= 1
        
        return True
