"""
We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.
"""
from collections import defaultdict
def enter_exit_records(logs):
    no_exits, no_enters = set(),set()
    records = defaultdict(list)
    for log in logs:
        records[log[0]].append(log[1])
    print(records)
    for employee, times in records.items():
        for i in range(1,len(times)):
            if times[i] == 'enter':
                if times[i-1] != 'exit':
                    no_exits.add(employee)
            else:
                if times[i-1]!= 'enter':
                    no_enters.add(employee)
        if times[0] == 'exit':
            no_enters.add(employee)
        if times[-1] != 'exit':
            no_exits.add(employee)
    return list(no_exits),list(no_enters)

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
