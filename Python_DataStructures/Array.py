class Array:
    def __init__(self, capacity):  # Initialize array with capacity (max size), current size(0), data(empty values at
        # indexes
        self.capacity = capacity  # How big the array can be
        self.size = 0  # Initialize size 0
        self.data = [None] * capacity  # Fill indexes with 0

    def insert(self, index, value):  # Insert values into array
        if self.size == self.capacity:  # If size == capacity, array is full
            raise OverflowError("Array is full")
        if index < 0 or index > self.size:  # If index is out of bounds
            raise IndexError("Index out of bounds")

        # Loop through array from end -> where new value with go, -1 index each#iteration
        for i in range(self.size, index, - 1):
            # Current data index value will equal the value of index - 1, shifting values right
            self.data[i] = self.data[i - 1]
        # Once at index, at intended value to index
        self.data[index] = value
        # Add 1 to size
        self.size += 1

    def delete(self, index):  # Delete values from array
        if index < 0 or index >= self.size:  # If index is out of bounds
            raise IndexError("Index out of bounds")
        # Loop through array form index value -> self.size - 1
        for i in range(index, self.size - 1):
            # Current data index value will equal the value of index + 1, shifting values left
            self.data[i] = self.data[i + 1]
        # Index of [self.size -1] value = None
        self.data[self.size - 1] = None
        # Subtract 1 from size
        self.size -= 1

    def sort(self):

        length = self.size - 1
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, length):
                if self.data[i] > self.data[i + 1]:
                    sorted = False
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
        return self

    def max(self):
        max_value = self.data[0]

        if self.size == 0:
            return Exception("No values in array")

        if self.size == 1:
            return f'Max Value: {max_value}'

        for i in range(0, self.size - 1):
            if self.data[i + 1] > max_value:
                max_value = self.data[i + 1]

        print(f'Max Value: {max_value}')

    def low(self):
        low_value = self.data[0]

        if self.size == 0:
            return Exception("No values in array")

        if self.size == 1:
            return f'Lowest Value: {low_value}'

        for i in range(0, self.size - 1):
            if self.data[i + 1] < low_value:
                low_value = self.data[i + 1]

        print(f'Lowest Value: {low_value}')

    def reverse(self):

        rev_arr = Array(self.capacity)
        j = 0

        for i in range(self.size - 1, -1, - 1):
            rev_arr.insert(j, self.data[i])
            j += 1
        print([rev_arr.data[i] for i in range(rev_arr.size)])

    def sum(self):

        sum_arr = 0

        if self.size == 0:
            return 'No values in array'

        if self.size == 1:
            return self.data(0)

        for i in range(self.size):
            sum_arr += self.data[i]

        print(f'Sum: {sum_arr}')

    def product(self):

        prod_arr = 1

        if self.size == 0:
            return 'No values in array'

        if self.size == 1:
            return self.data(0)

        for i in range(self.size):
            prod_arr *= self.data[i]

        print(f'Product: {prod_arr}')

    def display(self):  # Display array
        # Iterate through loop, printing each index value
        print([self.data[i] for i in range(self.size)])


arr = Array(5)

