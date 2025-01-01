class Stack:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)
    
    def peak(self):
        if self.is_empty():
            return 'empty'
        return self.array[-1]

    def pop_(self):
        if self.is_empty():
            return 'empty'
        self.array.pop()
    
    def is_empty(self):
        return len(self.array) == 0
    
    def size(self):
        return len(self.array)


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(5)
    stack.peak()
    stack.pop_()
    print(stack.array)