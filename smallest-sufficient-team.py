from collections import defaultdict
from math import inf
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # backtracking
        for i, skills in enumerate(people):
            people[i]=set(skills)
        # for every skill we need, we can consider every person who has this skills
        # => we need a skill-to-people dictionary

        # Optimization: one's skillset is a subset of another's
        # Only consider the person with a larger skillset
        for i, s1 in enumerate(people):
            for j, s2 in enumerate(people):
                if i!=j and s1.issubset(s2):
                    people[i]=set()
        # build skill-to-people dictionary
        STP = defaultdict(set)
        for i, skills in enumerate(people):
            for skill in skills: # skill_name
                STP[skill].add(i)

        # build backtracking engine
        self.needed = set(req_skills)
        self.smallest = inf
        res = []
        curr = [] # dynamic during backtracking algo
        def backtrack(i): 
            nonlocal res
            nonlocal curr # usually lists are globally mutable in a class method, not sure why this is needed
            if not self.needed:
                if self.smallest>len(curr):
                    self.smallest = len(curr)
                    res = curr.copy()
                return

            if req_skills[i] not in self.needed:
                backtrack(i+1)
                return

            for person in STP[req_skills[i]]: # person_index
                newSkills = people[person].intersection(self.needed)
                self.needed = self.needed - newSkills
                curr.append(person)

                backtrack(i+1)

                # backtrack
                curr.pop()
                self.needed=self.needed.union(newSkills)

        backtrack(0)
        return res