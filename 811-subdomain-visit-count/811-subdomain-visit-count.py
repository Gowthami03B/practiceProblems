import re
class Solution:
    def subdomainVisitsComplex(self, cpdomains: List[str]) -> List[str]:
        #extract digits for count
        #find the first dot and any other dots
        #store domain name as key and append to count in a map
        domain_count = defaultdict(int)
        for domain in cpdomains:
            count = re.search(r'^\d+', domain)
            count = count.group()
            domain = domain.replace(count,"")
            split_domains = domain.strip().split(".")
            domain_count[".".join(split_domains)] += int(count)
            n = len(split_domains)
            for i in range(1, n):
                domain_count[".".join(split_domains[i:n+1])] += int(count)
            
        print(domain_count)
        res = []
        for key, val in domain_count.items():
            res.append(str(val) + " " + key)
        return res
    
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for domain in cpdomains:
            domains = domain.split(" ")
            tpdomains = domains[1].split(".")
            for i in range(len(tpdomains)):
                domain_count[".".join(tpdomains[i:])] += int(domains[0])
        res = []
        for key, val in domain_count.items():
            res.append(str(val) + " " + key)
        return res