class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        friends_map = defaultdict(list)
        for idx, preference in enumerate(preferences):
            friends_map[idx] = preference
            
        # print(friends_map)
        
        preferences_map = defaultdict(list)
        for pair in pairs:
            preferences_map[pair[0]] = pair[1]
            preferences_map[pair[1]] = pair[0]

        print(preferences_map)
        unhappy_friends = set()
        for pair in pairs:
            x,y = pair[0],pair[1]
            preferences_x = friends_map[x]#1, 2,3,0
            pos_y = preferences_x.index(y)
            if pos_y != 0: # y is not 1st preference of x
                for i in range(pos_y):
                    u = preferences_x[i]#2
                    v = preferences_map[u]#0
                    preferences_u = friends_map[u]#1,3,0
                    pos_x_in_u = preferences_u.index(x)
                    pos_v_in_u = preferences_u.index(v)
                    if pos_x_in_u == 0 or (pos_x_in_u < pos_v_in_u):
                        unhappy_friends.add(x)
            
            preferences_y = friends_map[y]
            pos_x = preferences_y.index(x) 
            if pos_x != 0: 
                for i in range(pos_x):
                    u = preferences_y[i]
                    v = preferences_map[u]
                    preferences_u = friends_map[u]
                    pos_y_in_u = preferences_u.index(y)
                    pos_v_in_u = preferences_u.index(v)
                    if pos_y_in_u == 0 or (pos_y_in_u < pos_v_in_u):
                        unhappy_friends.add(y)
        print(unhappy_friends)
        return len(unhappy_friends)