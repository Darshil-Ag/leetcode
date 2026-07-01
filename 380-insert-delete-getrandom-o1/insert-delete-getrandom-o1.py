import random

class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val):
        if val in self.pos:
            return False

        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        # Move last element to deleted position
        self.arr[idx] = last
        self.pos[last] = idx

        # Remove last element
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.arr)