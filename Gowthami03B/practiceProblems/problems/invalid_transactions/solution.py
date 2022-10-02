class Solution:
    def invalidTransactions(self, transactions):
        hashmap = collections.defaultdict(list)
		#We will only store index of the transaction because the same transaction can repeat.
        result = set()
        for i, t in enumerate(transactions):
            name, time, amount, city =  t.split(",")
			#If there is no transaction record for the user
            if name not in hashmap:
                if int(amount) > 1000:
                    result.add(i)
			#If there are old tx records
            else:
				#Fetching past transaction from hashmap
                prevTrans = hashmap[name]
				#Iterating over the past transaction of the user and finding anomalies
                for j in range(len(prevTrans)):
                    prevName, prevTime, prevAmount, prevCity = transactions[prevTrans[j]].split(",")
                    if int(amount) > 1000:
                        result.add(i)
				#Checking whether it occurs within (and including) 60 min and diff city
                    if abs(int(time) - int(prevTime)) <= 60 and city != prevCity:
                        result.add(i)
                        result.add(prevTrans[j])
			#Recording transaction in the hashmap for the user
            hashmap[name].append(i)
		
		#Fetching transaction using indexes stored in the result set and returning
        return [transactions[t] for t in result]