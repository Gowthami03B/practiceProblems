"""

Given a dictionary that contains mapping of employee and his manager as a number of (employee, manager) pairs.
{ "A", "C" },
{ "B", "C" },
{ "C", "F" },
{ "D", "E" },
{ "E", "F" },
{ "F", "F" } 
In this example C is manager of A, 
C is also manager of B, F is manager 
of C and so on.
"""
from collections import defaultdict
def employeesUnderManager(emp_mgr):
    emp_mgr_map = defaultdict(list)
    for emp,mgr in emp_mgr:
        if emp != mgr:
            emp_mgr_map[mgr].append(emp)
    print(emp_mgr_map)

    def getEmps(emp,res,manager):
        for mgr in emp:
            if mgr in emp_mgr_map:
                res[manager] += len(emp_mgr_map[mgr])
                getEmps(emp_mgr_map[mgr],res,manager)

    res = defaultdict(int)
    for manager,emp in emp_mgr_map.items():
        res[manager] = len(emp)
        getEmps(emp,res,manager)

    return res

t = (("A", "C"),("B", "C"),("C", "F"),("D", "E"),("E", "F"),("F", "F"),("K","A"))
print(employeesUnderManager(t))
