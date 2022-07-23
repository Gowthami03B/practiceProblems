import itertools
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        packed_tuple = zip(timestamp, username, website) #create tuples with zip
        sorted_packed_tuple = sorted(packed_tuple) #sort tuples on timestamp
        """
        ["dowg","dowg","dowg"]
[158931262,562600350,148438945]
["y","loedo","y"]
        <zip object at 0x7f441b05ae80> [(148438945, 'dowg', 'y'), (158931262, 'dowg', 'y'), (562600350, 'dowg', 'loedo')]
[('y', 'y', 'loedo')]

        """
        user_website_map = defaultdict(list)
        for t, u, w in sorted_packed_tuple: # joe: ['home', 'about', 'career']  websites in list are in ascending timestamp order
            user_website_map[u].append(w)
        website_visits = defaultdict(int)
        print(user_website_map)
        for user, websites in user_website_map.items():
            combs = set(combinations(websites, 3)) #we need the set of combinations to not count duplicate ones
            for comb in combs:
                website_visits[comb] += 1
        print(website_visits)
        #now sort website_visits by val in desc, then lexicographical order
        # sorted_website_visits = sorted(website_visits.items(), key=lambda x: 
                                       # (-x[1], x[0]))
        # print(sorted_website_visits)#[(('home', 'about', 'career'), 2), (('cart', 'maps', 'home'), 1), (('home', 'cart', 'home'), 1), (('home', 'cart', 'maps'), 1), (('home', 'maps', 'home'), 1)]
        sorted_website_visits = sorted(website_visits, key=lambda x: 
                                       (-website_visits[x], x))
        # print(sorted_website_visits)#[('a', 'b', 'a'), ('a', 'b', 'c')]
        return sorted_website_visits[0]