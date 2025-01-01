class QueueArr:
    def __init__(self):
        self.array = []
    
    def enqueue(self, data):
        self.array.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return 'empty'
        self.array.pop(0)
    
    def peak(self):
        return self.array[0]
    
    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.array)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinked:
    def __init__(self):
        self.front = None
        self.rear = None
        self.queue_size = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.queue_size += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.queue_size += 1

    def dequeue(self, data):
        if self.is_empty():
            return 'empty'
        temp = self.front
        self.front = temp.next
        self.queue_size -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            return 'empty'
        return self.front.data

    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return self.queue_size

if __name__ == "__main__":
    que = QueueArr()
    que.enqueue(5)
    que.enqueue(5)
    que.enqueue(5)
    que.dequeue()
    print(que.array)