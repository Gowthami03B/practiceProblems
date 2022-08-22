from collections import defaultdict
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs= []
        letter_logs =[]
        for log in logs:
            # print(log)
            separated_logs = log.split(" ")
            if separated_logs[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key=lambda x: x.split()[0])#splits and sorts by identifiers
        letter_logs.sort(key=lambda x: x.split()[1:])#splits and sorts by letter logs
        
        letter_logs.extend(digit_logs)#append digit logs
        return letter_logs
            