import random
from sortedcontainers import SortedList

class Solution(object):
    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        blacklist_set = set(blacklist)
        self.sl = SortedList([i for i in range(n) if i not in blacklist])
        
    def pick(self):
        """
        :rtype: int
        """
        idx = random.randint(0, len(self.sl)-1)
        return self.sl[idx]
