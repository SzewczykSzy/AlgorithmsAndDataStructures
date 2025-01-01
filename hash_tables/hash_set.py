class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.hash_set = [[None] for i in range(size)]
    
    def hash_function(self, value):
        sum_of_chars = 0
        for char in value:
            sum_of_chars += ord(char)
        return sum_of_chars % self.size
    
    def add_element(self, value):
        idx = self.hash_function(value)
        bucket = self.hash_set[idx]
        if value not in bucket:
            bucket.append(value)
    
    def contains(self, value):
        idx = self.hash_function(value)
        bucket = self.hash_set[idx]
        return value in bucket
    
    def remove(self, value):
        idx = self.hash_function(value)
        bucket = self.hash_set[idx]
        if value in bucket:
            bucket.remove(value)
    
    def print_set(self):
        for idx, el in enumerate(self.hash_set):
            print(f"bucket {idx}: {el}")
    

if __name__ == "__main__":
    set_ = HashSet()
    set_.add_element('dbwu')
    print(set_.contains('sasa'))
    print(set_.contains('dbwu'))