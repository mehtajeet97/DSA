from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        #Sort the Input Arrays
        players.sort()
        trainers.sort()

        #Compare each array from start using two pointers
        i = j = 0

        # First pointer represents number of players matched
        while i < len(players):
            
            # Second pointer represents trainer skill level rn
            while j < len(trainers) and players[i] > trainers[j]:
                j = j+1

            if j == len(trainers):
                break

            i = i+1
            j = j+1

        return i
