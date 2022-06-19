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
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl.split('/')[2] #splits the string at /
        """
        ['http:', '', 'news.yahoo.com', 'news', 'topics', ''] news.yahoo.com
['http:', '', 'news.google.com'] news.google.com
        """
        print(startUrl.split('/'), hostname)
        queue = collections.deque([startUrl]) #start from startUrl
        visited = set([startUrl]) #add it to visited
        while queue:
            surl = queue.popleft()
            urls = htmlParser.getUrls(surl)#get the Urls
            for url in urls:
                if hostname in url and url not in visited:#if its the same host and not in visited
                    queue.append(url)
                    visited.add(url)
        return list(visited)
            