"""
Qn: Employees rank Teams and teams rank employees, find the best matches

Emp1 : [Team2, Team1, Team3] (preferences in order)
Emp2 : [Team1, Team3, Team2]
.
.
.
Team1 : [Emp3, Emp2, Emp1] (preferences in order)
Team2 : [Emp2, Emp1, Emp3]
.
.
How to match teams with employees based on this information?
"""
from collections import defaultdict
from heapq import heappop,heappush
def stableMatchEmpTeamMatch(emp_preferences, team_preferences):
    #employees and teams from 0 to n-1
    emp_map = defaultdict(list)
    team_map = defaultdict(list)
    for idx, preference in enumerate(emp_preferences):
        emp_map[idx] = preference

    for idx, preference in enumerate(team_preferences):
        team_map[idx] = preference
    minheap = []
    for emp in range(len(emp_preferences)):
        team_pref = emp_map[emp]#[1,0,2] of employee 0
        for t, team in enumerate(team_pref):
            emp_pref = team_map[team]#[1,0,2] of team 1
            pos_emp_in_team = emp_pref.index(emp)
            dist = pos_emp_in_team + t
            heappush(minheap, (dist,(emp,team)))
    pairs = []
    emp_set , team_set = set(),set()
    # print(minheap)
    while minheap:
        while minheap[0][1][0] in emp_set or minheap[0][1][1] in team_set:
            heappop(minheap)
            if len(minheap) == 0:
                break
        _, (emp,team) = heappop(minheap)
        pairs.append((emp, team))
        emp_set.add(emp)
        team_set.add(team)
        if len(pairs) == len(emp_preferences):
            break
    return pairs
emp_preferences = [[1, 0, 2],[0, 2, 1],[0,1,2]]
team_preferences =[[2, 1, 0],[1, 0, 2],[2,1,0]]
print(stableMatchEmpTeamMatch(emp_preferences, team_preferences))
