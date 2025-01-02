class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTreeArray:
    def __init__(self, size, data=None):
        self.arr = [None for i in range(size)] if not data else data
        self.size = size
    
    def right_child_idx(self, idx):
        return 2*idx + 2

    def left_child_idx(self, idx):
        return 2*idx+1
    
    def get_data(self, idx):
        if 0 <= idx <= self.size:
            return self.arr[idx] 
        else:
            return None
    
    def pre_order(self, idx):
        if idx >= self.size or self.arr[idx] is None:
            return []
        return [self.arr[idx]] + self.pre_order(self.left_child_idx(idx)) + self.pre_order(self.right_child_idx(idx))

    def in_order(self, idx):
        if idx >= self.size or self.arr[idx] is None:
            return []
        return self.in_order(self.left_child_idx(idx)) + [self.arr[idx]] + self.in_order(self.right_child_idx(idx))

    def post_order(self, idx):
        if idx >= self.size or self.arr[idx] is None:
            return []
        return self.post_order(self.left_child_idx(idx)) + self.post_order(self.right_child_idx(idx)) + [self.arr[idx]]


if __name__ == "__main__":
    n1 = Node(5)
    n2 = Node(6)
    n3 = Node(7)

    n2.right = n3
    n2.left = n1

    arr = ['R', 'A', 'B', 'C', 'D', 'E', 'F']
    binary_tree = BinaryTreeArray(len(arr), arr)
    l = binary_tree.left_child_idx(0)
    l = binary_tree.left_child_idx(l)
    print(binary_tree.get_data(l))
    print(binary_tree.pre_order(0))
    print(binary_tree.in_order(0))
    print(binary_tree.post_order(0))
