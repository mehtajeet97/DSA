from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Create result variable as length of either
        res = len(students)
        # Count the preferences of students in hashmap
        count = Counter(students)
        # Iterate through Sandwiches
        for s in sandwiches:
            # Check any student wants the first (index 0) sandwich
            if count[s] > 0:
                res -= 1
                count[s] -= 1
            else:
                return res

        return res
