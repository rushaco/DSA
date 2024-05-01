class HashTable:
    def __init__(self, size, replace=False):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.replace = replace

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.replace:
            for i, (k, _) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))
        else:
            for k, _ in self.table[index]:
                if k == key:
                    return  # Key already exists, do not insert
            self.table[index].append((key, value))

    def find(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True  # Key deleted successfully
        return False  # Key not found

def test_dictionary():
    # Create hash table without replacement
    table_without_replacement = HashTable(10, replace=False)

    # Insert values
    table_without_replacement.insert('Alice', '123456')
    table_without_replacement.insert('Bob', '987654')
    table_without_replacement.insert('Charlie', '555555')
    table_without_replacement.insert('David', '111222')

    # Find and delete values
    print("Value for key 'Alice':", table_without_replacement.find('Alice'))
    print("Value for key 'Charlie':", table_without_replacement.find('Charlie'))
    print("Deleting key 'Bob':", table_without_replacement.delete('Bob'))
    print("Value for key 'Bob':", table_without_replacement.find('Bob'))

    # Create hash table with replacement
    table_with_replacement = HashTable(10, replace=True)

    # Insert values
    table_with_replacement.insert('Alice', '123456')
    table_with_replacement.insert('Bob', '987654')
    table_with_replacement.insert('Charlie', '555555')
    table_with_replacement.insert('David', '111222')

    # Find and delete values
    print("Value for key 'Alice':", table_with_replacement.find('Alice'))
    print("Value for key 'Charlie':", table_with_replacement.find('Charlie'))
    print("Deleting key 'Bob':", table_with_replacement.delete('Bob'))
    print("Value for key 'Bob':", table_with_replacement.find('Bob'))


if __name__ == "__main__":
    test_dictionary()
