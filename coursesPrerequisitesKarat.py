"""
You're developing a system for scheduling advising meetings with students in a Computer Science program. Each meeting should be scheduled when a student has completed 50% of their academic program.

Each course at our university has at most one prerequisite that must be taken first. No two courses share a prerequisite. There is only one path through the program.

Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student will be taking when they are halfway through their program. (If a track has an even number of courses, and therefore has two "middle" courses, you should return the first one.)

Sample input 1: (arbitrarily ordered)
prereqs_courses1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

In this case, the order of the courses in the program is:
	Software Design
	Computer Networks
	Computer Architecture
	Data Structures
	Algorithms
	Foundations of Computer Science
	Operating Systems

Sample output 1:
	"Data Structures"

Sample input 2:
prereqs_courses2 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
]

Sample output 2:
	"Foundations of Computer Science"

Sample input 3:
prereqs_courses3 = [
	["Data Structures", "Algorithms"],
]

Sample output 3:
	"Data Structures"

Complexity analysis variables:

n: number of pairs in the input

prereqs_courses1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

figure out order of taking courses
then middle course

AL -> FCS -> OS
CA -> DS -> AL
SD -> CN -> CA

"""
prereqs_courses1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

def courseOrder(courses):
    if not courses:
	    return None

    graph = {}
    for start, end in courses:
	    graph[start] = end
    #print(graph) #build adjacency list
    sortedCourses = []
    visited = set()
    def topSort(course):
            if course in visited: #if visited need not do anything
                return
            elif course in graph:
                print(f"topSort({course}, {graph[course]})") 
                #if course is in graph means it is dependent on another course
                topSort(graph[course]) #graph[foundations of CS] == OS (explore OS next), if its the leaf node, then it won't have
                #any more branches, add to visted and sorted
                #OS is dependent on FCS, but are there any courses dependent on OS? hence check for is course in graph?
                #we repeat until the branch is completely explored
            sortedCourses.append(course)
            visited.add(course)
            print(sortedCourses, visited)

    for course in graph.keys():
            topSort(course) #start from the keys of graph

    sortedCourses.reverse()

    print(sortedCourses)

    index = len(sortedCourses) // 2
    if len(sortedCourses) % 2 == 0:
        index -= 1
    return sortedCourses[index]
print(courseOrder(prereqs_courses1))
