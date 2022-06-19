# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum1(self, nestedList: List[NestedInteger]) -> int:
        depthMap = collections.defaultdict(list)
        depth = 1
        totSum = 0
        def dfs(nestedList, depth):
            for item in nestedList:
                if item.isInteger():
                    depthMap[depth].append(item)
                else:
                    dfs(item.getList(), depth + 1)
        dfs(nestedList, depth)
        print(depthMap)
        for key, values in depthMap.items():
            for val in values:
                if not val.getList():
                    totSum += key * int(val.getInteger())
        return totSum
    
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            totSum = 0
            for item in nestedList:
                if item.isInteger():
                    totSum += item.getInteger() * depth
                else:
                    totSum += dfs(item.getList(), depth + 1)
            return totSum
        
        return dfs(nestedList, 1)
        