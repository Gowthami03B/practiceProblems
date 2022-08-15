from abc import ABC, abstractmethod
from enum import Enum
import re

class log_message_types(Enum):
    ERROR,SUCCESS ="transmit error",  "sent message"

class File():
    def __init__(self,name,size):
        self.name=name
        self.size=size

    def writeToFile(self,file,text):
        pass

class LogFileReader(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def readLogFile(self, file):
        pass

class readLogsFromTextFiles(LogFileReader):
    def __init__(self):
        pass

    def readLogFile(self,file):
        #read file, get it into a string
        pass

class LogFileParser(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def parse(self,logs):
        pass

class ParseByError(LogFileParser):
    def __init__(self,errorText):
        self.errorText=errorText

    def parse(self,logs):
        pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\s+\w+\s+\w+")
        list_logs = pattern.findall(logs)
        filtered_logs = []
        for log in list_logs:
            if log.endswith(self.errorText):
                filtered_logs.append(log)
        return filtered_logs, len(filtered_logs)

f1 = File("log1.txt",1000)
f2 = File("log2.txt",1000)
reader = readLogsFromTextFiles()
reader.readLogFile(f1)
logs = """2018-10-23T09:35:29Z sent message
2018-10-23T09:44:01Z transmit error
2018-10-23T09:49:29Z sent message
2018-10-23T10:01:49Z sent message
2018-10-23T10:05:29Z transmit error
2018-10-23T10:06:05Z transmit error
2018-10-23T10:07:17Z transmit error
2018-10-23T11:23:24Z sent message
2018-10-23T11:52:28Z sent message
2018-10-23T12:01:13Z transmit error"""
parser = ParseByError(log_message_types.ERROR.value)
print(parser.parse(logs))


