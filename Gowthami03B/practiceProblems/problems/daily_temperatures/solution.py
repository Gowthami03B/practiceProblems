class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
         # Pop until the current day's temperature is not warmer than the temperature at the top of the stack
            # On each day, there are two possibilities. If the current day's temperature is not warmer than the temperature on the top of the stack, we can just push the current day onto the stack - since it is not as warm (equal or smaller), this will maintain the sorted property (decreasing stack).
            # If the current day's temperature is warmer than the temperature on top of the stack, this is significant. It means that the current day is the first day with a warmer temperature than the day associated with the temperature on top of the stack. Hence we pop and diff between indices is the no of days for a warmer temp
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer
