"""
We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.
"""
from collections import defaultdict
def recordEntryExitTimes(records):
    records_map = defaultdict(list)
    for name, record in records:
        records_map[name].append(record)
    no_exits = set()
    no_enters = set()
    print(records_map)
    for name, times in records_map.items():
        stack_times = []
        for time in times:
            if time == "exit":
                topEle = stack_times.pop() if stack_times else '#'
                if topEle != "enter":
                    no_enters.add(name)
            else:
                stack_times.append(time)
        if len(stack_times) > 0:
            no_exits.add(name)
    print(no_exits, no_enters)

records1 = [
["Martha", "exit"],
["Paul", "enter"],
["Martha", "enter"],
["Steve", "enter"],
["Martha", "exit"],
["Jennifer", "enter"],
["Paul", "enter"],
["Curtis", "exit"],
["Curtis", "enter"],
["Paul", "exit"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "exit"],
["Paul", "enter"],
["Paul", "enter"],
["Martha", "exit"],
["Paul", "enter"],
["Paul", "enter"],
["Paul", "exit"],
["Paul", "exit"]
] 
records2 = [
["Paul", "enter"],
["Paul", "exit"],
]


records3 = [
["Paul", "enter"],
["Paul", "enter"],
["Paul", "exit"],
["Paul", "exit"],
]


records4 = [
["Paul", "enter"],
["Paul", "exit"],
["Paul", "exit"],
["Paul", "enter"],
]
print(recordEntryExitTimes(records1))
print(recordEntryExitTimes(records2))
print(recordEntryExitTimes(records3))
print(recordEntryExitTimes(records4))
