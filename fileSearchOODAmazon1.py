from abc import ABC,abstractmethod
import collections
from enum import Enum
class Operator(Enum):
    Equal, LessThan, GreaterThan = 0,1,2
class File:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.is_directory = True if "." not in name else False
        self.children=[]
        self.extension=name.split(".")[1] if "." in name else ""

class Specification(ABC):
    def __init__(self):
        pass
    def is_satisfied(self):
        pass
    def __and__(self):
        return CombinedSpecification(self,other)

class CombinedSpecification(Specification):
    def __init__(self, first:Specification,second:Specification):
        self.first = first
        self.second = second

    def is_satisfied(self, file):
        return self.first.is_satisfied(file) and self.second.is_satisfied(file)

class ExtensionSpecification(Specification):
    def __init__(self, extension):
        self.extension = extension
    def is_satisfied(self, file):
            return self.extension == file.extension

class SizeSpecification(Specification):
    def __init__(self, size, operator):
        self.size = size
        self.operator =operator

    def is_satisfied(self, file):
        if self.operator == Operator.Equal:
                return file.size == self.size
        elif self.operator == Operator.LessThan:
                return file.size > self.size
        else:
                return file.size < self.size
        return False

class FileSearch():
    def __init__(self, files):
        self.files = files
        self.filtered_files = []

    def searchFiles(self, searchCriteria:Specification):
        queue = collections.deque(self.files)
        while queue:
            curr = queue.popleft()
            if curr.is_directory:
                    for child in curr.children:
                        queue.append(child)
            else:
                    if searchCriteria.is_satisfied(curr):
                        self.filtered_files.append(curr.name)
        return self.filtered_files

root = File('home', 10)
f1 = File('abc.txt', 2)
f2 = File('bcd.txt', 5)
f3 = File('def.cls', 10)
f4 = File('abc.txt', 10)
root.children=[f1,f2,f3,f4]
filter_txt = ExtensionSpecification("txt")
filter_size=SizeSpecification(10, 2)
combined_filter=filter_txt.__and__(filter_size)
files = [root]
fileSearch = FileSearch(files)
print(fileSearch.searchFiles(filter_size))
print(fileSearch.searchFiles(combined_filter))
     
