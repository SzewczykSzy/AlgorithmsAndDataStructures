class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.hash_set = [[None] for i in range(size)]
    
    def hash_function(self, value):
        sum_of_chars = 0
        for char in value:
            sum_of_chars += ord(char)
        return sum_of_chars % self.size
    
    def add_element(self, key, value):
        idx = self.hash_function(key)
        bucket = self.hash_set[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key):
        idx = self.hash_function(key)
        bucket = self.hash_set[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v
        return None
    
    def remove(self, key):
        idx = self.hash_function(key)
        bucket = self.hash_set[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
    
    def print_map(self):
        for idx, el in enumerate(self.hash_set):
            print(f"bucket {idx}: {el}")
    

if __name__ == "__main__":
    pass