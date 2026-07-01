import random
from collections import defaultdict

class Solution(object):

    def __init__(self, nums):
        self.mp = defaultdict(list)

        for i, num in enumerate(nums):
            self.mp[num].append(i)

    def pick(self, target):
        return random.choice(self.mp[target])