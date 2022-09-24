class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0:
            return 0
        
        tax = prev = 0
        for upper, percent in brackets:
            if income >= upper:#income doesn't change
                tax += (upper - prev) * percent / 100
                prev = upper#so upper no of dollars are already taxed
            else:
                tax += (income - prev) * percent / 100#remaining dollars = income-prev
                return tax
        return tax    
        