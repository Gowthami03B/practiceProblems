"""Given a book with a finite number of pages. At each page, it can be either empty or contain 2 options, each option represent the page number that readers must jump to to continue reading, if the page does not have any option, simply go to the next page. if the options is available at a page, readers have to pick one. The book has multiple ending pages, if an ending page is reached, no further reading is needed.

Question 1:
Given endingPages, pageOptions, optionToPick, write a function that take in all these arguments and return the ending page. if the pageOption somehow lead to an infinite loop, return -1. Assume that readers can always reach one ending of infinite loop does not happen.

Example: happy path

endingPages - [9,15, 20] -> array of integer
pageOption - [ [3,5,11] ] -> An array that contains multple ingeter array with format of [this page number has options, option 1, option 2]
[3,5,11] means that at page 3, there are 2 options, option 1 is to jump to page 5, option 2 is to jump to page 11.
optionToPick - 1 -> an integer that tells readers which option they have to pick. with optionToPick as 1 and with pageOption [ [3,5,11], [21, 30, 39] ], this means that at page 3 readers have to jump to page 5, at page 21 readers have to jump to page 30.
1-2-3-5-6-7-8-9 -> at page 1 go to 2 because page 1 has no option. do the same for page 2. at page 3 go to page 5 because readers have to pick option 1, continue to page 9 which is an ending, we stop here and return 9 as result

Example: infinite loop

endingPages - [9,15, 20]
pageOption - [ [3,5,11], [7, 1 , 20] ]
optionToPick - 1
1-2-3-5-6-7-1...
return -1 as result because we hit infinite loop here.

Question 2:
optionToPick is no longer available, readers can freely pick any option. write a function (or edit the code from question 1) that take in goodEndingPages, badEndingPages, pageOptions, and return all possible good ending that can be reached. Assume that at least 1 good ending can always be reached.
NOTE: if a bad ending is reached, readers cannot read further. If and infinite loop occures, simply avoid that route.

goodEndingPages - [9,15, 30]
badEndingPages - [17, 25]
pageOption - [ [3,5,11], [13, 15,17] ]
Good ending(s) route -> 1-2-3-5-6-7-8-9, 1-2-3-11-12-13-15
bad ending(s) route -> 1-2-3-11-12-13-17 -> no further reading.

The Karat process was quick, Karat interviewer was nice. I talked through my approach, coded it all out. I did coded the solution for Question 2 but did not get a chance to test it before times run out, not sure what I wrote work but I did get to onsite with Indeed."""
from collections import defaultdict
def pages(endingPages, pageOptions, optionToPick):
    startPage = pageOptions[0][0]
    endingPagesSet = set(endingPages)
    pagesVisited = set()
    prevPage = 1
    
    pageOptions.sort()
    for i in range(len(pageOptions)):
        currPage = pageOptions[i][0] 
        for j in range(prevPage,currPage + 1):
            if j in endingPagesSet:
                return j
            pagesVisited.add(j)
        nextPage = pageOptions[i][optionToPick]
        if nextPage in endingPagesSet:
            return nextPage
        pagesVisited.add(nextPage)
        prevPage = nextPage + 1
    print(pagesVisited)

endingPages =[9,15, 20]
pageOptions =[ [21, 30, 39],[3,5,11] ] 
option = 1
# print(pages(endingPages, pageOptions, 2))

def allGoodEndings(goodEndingPages, badEndingPages, pageOptions):
    goodEndingPagesSet = set(goodEndingPages)
    badEndingPagesSet = set(badEndingPages)
    nextPgOptions = defaultdict(list)
    for curr, next1, next2 in pageOptions:
        nextPgOptions[curr].extend([next1,next2])
    print(nextPgOptions)
    reachable = set()
    def dfs(page, seen):
        if page in badEndingPagesSet or page in seen:
            return
        seen.add(page)
        if page in goodEndingPagesSet:
            reachable.add(page)
            goodEndingPagesSet.remove(page)
            print(seen)
        if page not in nextPgOptions:
            dfs(page + 1, seen)
        else:
            for option in nextPgOptions[page]:
                dfs(option, seen)

    dfs(1,set())
    return reachable

goodEndingPages = [9,15, 30]
badEndingPages = [17, 25]
pageOptions = [ [3,5,11], [13, 15,17] ]
print(allGoodEndings(goodEndingPages, badEndingPages, pageOptions))


    
