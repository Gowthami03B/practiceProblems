"""
We are working on a security system for a badged-access room in our company's building.

We want to find employees who badged into our secured room unusually often. We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, such as "800" or "2250".

Write a function that finds anyone who badged into the room three or more times in a one-hour period. Your function should return each of the employees who fit that criteria, plus the times that they badged in during the one-hour period. If there are multiple one-hour periods where this was true for an employee, just return the earliest one for that employee.
"""
from collections import defaultdict
def badgeTimesKarat(badge_times):
    res = defaultdict(list)
    person_entry_map = defaultdict(list)
    for name, time in badge_times:
        time_mins = 0
        if len(time) != 3:
            time_mins = int(time[:2]) * 60 
        elif len(time) == 3:
            if int(time[:2]) > 9 and int(time[:2]) < 24:
                time_mins = int(time[:2]) * 60
                if time[2:]:
                    time_mins += int(time[2:])
            else:
                time_mins = int(time[:1]) * 60
                if time[1:]:
                    time_mins += int(time[1:])
        if time[2:]:
            time_mins += int(time[2:])
        person_entry_map[name].append((time, time_mins))
    print(person_entry_map)

    for name, times in person_entry_map.items():
        times.sort(key = lambda x: x[1])
        # print(name, times)
        s,e = 0,0 
        max_count = 0
        while e < len(times):
            if times[e][1] - times[s][1] <= 60: 
                max_count = max(max_count, e - s + 1)
                if max_count >= 3:
                    res[name].append([times[i][0] for i in range(s,e+1)])
                e += 1
            else:
                s += 1
                max_count = 0
    return res

x = [1,1,1,1,1,2]
print(list(set(x)))
badge_times = [
["Paul", "1355"], ["Jennifer", "1910"], ["Jose", "835"],
["Jose", "830"], ["Paul", "1315"], ["Chloe", "0"],
["Chloe", "1910"], ["Jose", "1615"], ["Jose", "1640"],
["Paul", "1405"], ["Jose", "855"], ["Jose", "930"],
["Jose", "915"], ["Jose", "730"], ["Jose", "940"],
["Jennifer", "1335"], ["Jennifer", "730"], ["Jose", "1630"],
["Jennifer", "5"], ["Chloe", "1909"], ["Zhang", "1"],
["Zhang", "10"], ["Zhang", "109"], ["Zhang", "110"],
["Amos", "1"], ["Amos", "2"], ["Amos", "400"],
["Amos", "500"], ["Amos", "503"], ["Amos", "504"],
["Amos", "601"], ["Amos", "602"], ["Paul", "1416"],
];
print(badgeTimesKarat(badge_times))
