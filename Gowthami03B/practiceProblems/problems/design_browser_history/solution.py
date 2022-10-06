from collections import deque

class BrowserHistory:

    def __init__(self, homepage: str):
	
        self.history = deque([homepage])
        self.cur_index = 0
        
    def visit(self, url: str) -> None:
        # clear all forward history
        tail_len = len(self.history)-1-self.cur_index
        while tail_len:
            self.history.pop()
            tail_len -= 1
            
        self.history.append(url)
        self.cur_index += 1
        
    def back(self, steps: int) -> str:
        
		# boundary check
        if steps > self.cur_index:
            self.cur_index = 0
        else:
            self.cur_index -= steps
            
        return self.history[self.cur_index]
    
    def forward(self, steps: int) -> str:
        # boundary check
        if steps >= len(self.history) - self.cur_index:
            self.cur_index = len(self.history) - 1
        else:
            self.cur_index += steps
        
        return self.history[self.cur_index]