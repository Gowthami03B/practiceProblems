class TimeMap:

    def __init__(self):
        self.key_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        list_values = self.key_store[key]
        if len(list_values) == 0:
            return ""
        if list_values[0][0] > timestamp:
            return ""
        if list_values[-1][0] <= timestamp:
            return list_values[-1][1]
        start,end= 0, len(list_values)-1
        while(start <= end):
            mid = (start + end)//2
            if list_values[mid][0] == timestamp:
                return list_values[mid][1]
            elif list_values[mid][0] > timestamp:
                end = mid - 1
            else:
                start = mid + 1
        return list_values[start-1][1]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)