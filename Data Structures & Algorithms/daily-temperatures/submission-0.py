class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        for i in range(len(temperatures)):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] - temperatures[i] > 0:
                    break
                
                j += 1
                count += 1
            
            if j == n:
                count = 0
            else:
                count
            res.append(count)
        
        return res