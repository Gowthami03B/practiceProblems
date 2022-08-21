class FileSystem:

    def __init__(self):
        self.trie = {}
    # the $ key is used to distinguish between a file path (which has a $ key) and a directory path (which doesn't have a $ key). The content of the file is stored in this $ key
    def traverseTo(self, path):
        dirs = [''] if path == '/' else path.split('/')
        node = self.trie
        for d in dirs:
            node = node.setdefault(d, {})#The setdefault() method returns the value of the item with the specified key.If the key does not exist, insert the key, with the specified value
        return node

    def ls(self, path: str) -> List[str]:#O(m+n+k. log k) - m(len of path to split into dirs),#n - depth of directories to travel, we sort the keys hence k log k
        dirs = [''] if path == '/' else path.split('/')
        node = self.trie
        for path in dirs:
            if path not in node:
                return None
            node = node[path]
        if '$' in node: return [dirs[-1]]
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:#O(m+n) - m len of path, n depth of directories to traverse to create, same for addContent and removeContent
        self.traverseTo(path)
            
    def addContentToFile(self, filePath: str, content: str) -> None:
        file = self.traverseTo(filePath)
        if '$' in file: file['$'] += content#if a file is found, then we get $, we append content 
        else: file['$'] = content#else we create it

    def readContentFromFile(self, filePath: str) -> str:
        file = self.traverseTo(filePath)
        return file['$']


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)