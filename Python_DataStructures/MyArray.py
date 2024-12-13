class MyArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def insert(self, index, value):
        if self.size >= self.capacity:
            raise OverflowError("Array is full")
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def display(self):
        print([self.data[i] for i in range(self.size)])


# Example Usage
arr = MyArray(5)
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
arr.display()  # Output: [10, 20, 30]
arr.delete(1)
arr.display()  # Output: [10, 30]
