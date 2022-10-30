from collections import defaultdict
class Solution:
    def invalidTransactions1(self, transactions: List[str]) -> List[str]:
        transaction_map = defaultdict(list)
        invalid = []
        
        for tx in transactions:
            name, time, amount, city = tx.split(",")
            if int(amount) > 1000:
                invalid.append(tx)
            if name in transaction_map:
                flag = False
                for prev in transaction_map[name]:
                    p_name, p_time, p_amount, p_city = prev.split(",")
                    if p_city != city and abs(int(p_time)- int(time)) < 60:
                        flag=True
                        invalid.append(prev)
                    
                if flag:
                    invalid.append(tx)                
            
            transaction_map[name].append(tx)
            
        print(invalid)
        return invalid
    
    def invalidTransactions1(self, arr: List[str]) -> List[str]:
        self.memo = collections.defaultdict(list)
        ans = set()
        for s in arr:
            name, mi, mon, place = s.split(",")
            if int(mon) > 1000:
                ans.add(s)
            if self.memo[name]:
                flag = False
                for a,b,c,d in self.memo[name]:
                    if d != place and abs(int(mi) - b) <= 60:
                        flag = True
                        ans.add(a + "," + str(b) + "," + str(c) + "," + d)
                if flag:
                    ans.add(s)
            self.memo[name] += ((name, int(mi), int(mon), place)),
        return ans
    
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if len(transactions) == 1: return transactions
        transactions = sorted(transactions)
        print(transactions)
        n = len(transactions)
        invalid = set()

        for i in range(n):
            name1, time1, amount1, city1 = transactions[i].split(',')
            if int(amount1) > 1000:
                invalid.add(i)

            for j in range(i+1, n):
                name2, time2, amount2, city2 = transactions[j].split(',')
                if name1 != name2:
                    break
                if int(amount2) > 1000:   
                    invalid.add(j)
                if city1 != city2 and abs(int(time2) - int(time1)) <= 60:
                    invalid.add(i)
                    invalid.add(j) 

        result = []
        for i, transaction in enumerate(transactions): 
            if invalid.__contains__(i):
                result.append(transaction)
        return result