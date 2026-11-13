
# Below is the interface for Iterator.
# class Iterator:
#     def __init__(self, nums):
#     def hasNext(self):
#     def next(self):

class PeekingIterator(object):

    def __init__(self, iterator):
        self.iterator = iterator
        self.next_element = None
        self.has_next_element = iterator.hasNext()

        if self.has_next_element:
            self.next_element = iterator.next()

    def peek(self):
        return self.next_element

    def next(self):
        current = self.next_element

        self.has_next_element = self.iterator.hasNext()

        if self.has_next_element:
            self.next_element = self.iterator.next()
        else:
            self.next_element = None

        return current

    def hasNext(self):
        return self.has_next_element
