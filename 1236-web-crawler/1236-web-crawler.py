# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import re
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl.split('/')[2]
        print(startUrl.split('/'), hostname)
        queue = collections.deque([startUrl])
        visited = set([startUrl])
        while queue:
            surl = queue.popleft()
            urls = htmlParser.getUrls(surl)
            for url in urls:
                if url.split('/')[2] == hostname and url not in visited:
                    queue.append(url)
                    visited.add(url)
        return list(visited)
            