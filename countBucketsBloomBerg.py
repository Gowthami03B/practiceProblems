"""
Given a list of tuples default buckets and a list of scores, compare each item in scores with every tuple in default_bucket and count how many fall under such buckets. Output has to be a dictionary with tuple as keys and the count as values.

default_bucket = [(300,400), (401, 500), (501, 600), (601, 700), (701, 800), (801, 900), (901, 1000)]

scores = [420, 410, 908, 700, 450, 310, 200, 555, 996, 1000]

output = {(300, 400): 2, (401, 500): 3, (501, 600): 1, (601, 700): 1, (901, 1000): 3}
eg: 420 is lt 500 and gt 401 so the count of (401, 500) increases by 1.
410 falls between 401 and 500 so count increments by 1.
450 falls 401 and 500 so count increments by 1. So the count for this tuple is 3 .
"""
from collections import defaultdict
def countBuckets(default_bucket, scores):#O(n log n) + O(m.log n)== o(MAX(M,N) LOG N)
    default_bucket.sort()
    bucket_counts =defaultdict(int)
    for target in scores:
        s ,e = 0, len(default_bucket) - 1
        while(s <= e):
            mid = (s+e)//2
            upper, lower =default_bucket[mid][0],default_bucket[mid][1]
            if target >=upper  and target <= lower:
                bucket_counts[(upper, lower)] += 1
                break
            elif target <= upper:
                e = mid - 1
            else:
                s = mid + 1
        if e < 0 or s >= len(default_bucket):
            if e < 0:
                upper, lower =default_bucket[s][0],default_bucket[s][1]
            else:
                upper, lower =default_bucket[e][0],default_bucket[e][1]
            bucket_counts[(upper, lower)] += 1
    return bucket_counts

def countBucketsTwoPointers(default_bucket, scores):
    pass

default_bucket = [(300,400), (401, 500), (501, 600), (601, 700), (701, 800), (801, 900), (901, 1000)]

scores = [2000, 420, 410, 908, 700, 450, 310, 200, 555, 996, 1000]
print(countBuckets(default_bucket,scores))
