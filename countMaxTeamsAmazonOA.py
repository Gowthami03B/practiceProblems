"""
Each team will have exactly N team size.
Skill of i th person will be denoted by skill[i] array.
Diff. between the maximum and minimum skill levels within a team cannot exeed a thershold, K.
Eg : skill = [6,1,3,4,3,5]
N = 3
K = 2

Output = 2
Explanation : Two teams can be formed [1,3,3] and [6,4,5] with difference between max and min skills not exceeding K = 2 value.
"""
def countMaxTeams(nums, teamSize, maxDiff):
    teams = 0
    n = len(nums)
    if n < teamSize:
        return teams
    
    nums.sort()
    i = 0
    while(i < n):
        if i + teamSize - 1 < n:
            diff = nums[i+teamSize-1] - nums[i] #[1,3,3,4,5,6] diff between max and min in 1st team
            if diff <= maxDiff:
                teams += 1
                i += teamSize#basically we can form only n/teamSize number of teams, once we find the diff between max and min in 1st team, need to move to 2nd
                continue
        i += 1
    return teams

nums =  [3,4,3,1,6,5]
teamSize = 3
maxDiff = 1
print(countMaxTeams(nums, teamSize, maxDiff))
