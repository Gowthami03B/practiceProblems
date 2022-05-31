from collections import defaultdict
from collections import deque
import itertools
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        recipe_ingredients = defaultdict(list)
        res = []
        indegree = defaultdict(int)
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                recipe_ingredients[ingredient].append(recipes[i])
                indegree[recipes[i]] +=1 
                if ingredient not in recipes:
                    indegree[ingredient] = 0
        print(recipe_ingredients, indegree)   
        count = 0
        queue = deque()
        visited = set()
        for key,val in indegree.items():
            if val == 0 and key not in visited and key in supplies:
                queue.append(key)
            while(queue):
                ele = queue.popleft()
                if indegree[ele] == 0:
                    count += 1
                    visited.add(ele)
                for child in recipe_ingredients[ele]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)
                        
        for recipe in recipes:
            if recipe in visited:
                res.append(recipe)
        return res
            
            