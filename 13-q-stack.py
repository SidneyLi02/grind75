class MyQueue(object):

    def __init__(self):
        self.q = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        aux = []
        while len(self.q) > 0:
            el = self.q.pop()
            aux.append(el)

        ret = aux.pop()
        while len(aux) > 0:
            el = aux.pop()
            self.q.append(el)
        return ret
        

    def peek(self):
        """
        :rtype: int
        """
        aux = []
        while len(self.q) > 0:
            el = self.q.pop()
            aux.append(el)

        ret = aux[-1] # peek
        while len(aux) > 0:
            el = aux.pop()
            self.q.append(el)
        return ret
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()