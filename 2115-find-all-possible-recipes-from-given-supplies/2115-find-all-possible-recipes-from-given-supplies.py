from collections import defaultdict
from collections import deque
import itertools
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        recipe_ingredients = defaultdict(list) #adjancency list
        res = [] 
        indegree = defaultdict(int) #indegree for all ingredients
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                recipe_ingredients[ingredient].append(recipes[i]) #adjacency list between ingredient:recipe
                indegree[recipes[i]] +=1 #that recipe indegree
                if ingredient not in recipes:
                    indegree[ingredient] = 0 #set independent ingredients indegree to 0
        print(recipe_ingredients, indegree)   
        queue = deque()
        visited = set()
        for key,val in indegree.items():
            if val == 0 and key not in visited and key in supplies: #start with indegree 0 and not in visited and make sure that item is in supplies
                queue.append(key)
            while(queue):
                ele = queue.popleft()
                if indegree[ele] == 0:
                    visited.add(ele)#add to visited
                for child in recipe_ingredients[ele]:#for each recipe that's dependent on a ingredient
                    indegree[child] -= 1#reduce indgeree of recipe dependent on that ingredient
                    if indegree[child] == 0:
                        queue.append(child)
                        
        for recipe in recipes:
            if recipe in visited:#if recipe in visited, it can be prepared
                res.append(recipe)
        return res
            
            