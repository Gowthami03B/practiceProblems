class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmail = set()
        
        for email in emails:
            localName = []
            for currChar in email:
                if currChar == '+' or currChar == '@':
                    break
                    
                if currChar != '.':
                    localName.append(currChar)            
                
            
            domainName = []
            for domainChar in reversed(email):
                domainName.append(domainChar)
                if domainChar == '@':
                    break
                    
            localName = ''.join(localName)
            domainName = ''.join(reversed(domainName))
            uniqueEmail.add(localName + domainName)
            print (uniqueEmail)
            
        return len(uniqueEmail)