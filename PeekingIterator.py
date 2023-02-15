class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.temp_value = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self.temp_value

    def next(self):
        ret_value = self.temp_value
        self.temp_value = self.iterator.next() if self.iterator.hasNext() else None
        return ret_value

    def hasNext(self):
        return self.temp_value is not None
