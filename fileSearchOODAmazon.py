"""
Design Unix File Search API to search file with different arguments as "extension", "name", "size" ...
The design should be maintainable to add new contraints.

Follow up: How would you handle if some contraints should support AND, OR conditionals.

"""
from abc import ABC,abstractmethod
import collections
class File:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.is_directory = True if "." not in name else False
        self.children=[]
        self.extension=name.split(".")[1] if "." in name else ""

class Filter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def filter(self,file):
        pass

class FilterByExtension(Filter):
    def __init__(self,extension):
        self.extension = extension
    
    def filter(self,file):
        return file.extension == self.extension

class FilterByFileSize(Filter):
    def __init__(self,size):
        if size < 0:
            raise ValueError("size cannot be negative")
        self.size = size
    
    def filter(self,file):
        return file.size >= self.size

class LinuxFind():
    def __init__(self):
        self.filters:List[Filter] = []

    def addFilter(self,filter):
        if isinstance(filter, Filter):
            self.filters.append(filter)

    def apply_or_filtering(self,root):
        filesFound = set()
        queue = collections.deque([root])
        while queue:
            curr = queue.popleft()
            if curr.is_directory:
                for child in curr.children:
                    queue.append(child)
            else:
                for filter in self.filters:
                    if filter.filter(curr):
                        filesFound.add(curr.name)
        return list(filesFound)

    def apply_and_filtering(self,root):
        filesFound = set()
        queue = collections.deque([root])
        while queue:
            curr = queue.popleft()
            if curr.is_directory:
                for child in curr.children:
                    queue.append(child)
            else:
                is_found = True
                for filter in self.filters:
                    if not filter.filter(curr):
                        is_found = False
                if is_found:
                    filesFound.add(curr.name)
        return list(filesFound)


f1 = File("root_300", 300)

f2 = File("fiction_100", 100)
f3 = File("action_100.txt", 100)
f4 = File("comedy_100", 100)
f14=File("comedy_100.txt", 100)
f1.children = [f2, f3, f4,f14]

f5 = File("StarTrek_4.txt", 4)
f6 = File("StarWars_10.xml", 10)
f7 = File("JusticeLeague_15.txt", 15)
f8 = File("Spock_1.jpg", -1)
f2.children = [f5, f6, f7, f8]

f9 = File("IronMan_9.txt", 9)
f10 = File("MissionImpossible_10.rar", 10)
f11 = File("TheLordOfRings_3.zip", 3)
f3.children = [f9, f10, f11]

f11 = File("BigBangTheory_4.txt", 4)
f12 = File("AmericanPie_6.mp3", 6)
f4.children = [f11, f12]

filter_by_txt = FilterByExtension("txt")#can exist without LinuxFind
filter_by_size = FilterByFileSize(-1)
findFiles = LinuxFind()
findFiles.addFilter(filter_by_txt) #aggregation
findFiles.addFilter(filter_by_size)#aggregation
print(findFiles.apply_or_filtering(f1))
print(findFiles.apply_and_filtering(f1))
