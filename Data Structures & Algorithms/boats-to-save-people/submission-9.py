class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        l = 0
        r = len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r -= 1

            if l <= r and remain >= people[l]:
                l += 1
            count += 1
        return count