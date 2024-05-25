class DynamicArray:
    def __init__(self, factor=2):
        self.factor = factor
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert_at_index(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self._resize(self.capacity * self.factor)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = val
        self.size += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        if self.size < self.capacity // self.factor:
            self._resize(self.capacity // self.factor)

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        self.array = self.array[::-1]

    def append(self, val):
        if self.size == self.capacity:
            self._resize(self.capacity * self.factor)
        self.array[self.size] = val
        self.size += 1

    def prepend(self, val):
        self.insert_at_index(0, val)

    def merge(self, other):
        while self.size + other.size > self.capacity:
            self._resize(self.capacity * self.factor)
        for val in other.array[:other.size]:
            self.array[self.size] = val
            self.size += 1

    def interleave(self, other):
        result = DynamicArray(factor=self.factor)
        length = min(self.size, other.size)
        for i in range(length):
            result.append(self.array[i])
            result.append(other.array[i])
        if self.size > length:
            result.merge(DynamicArray(self.array[length:]))
        elif other.size > length:
            result.merge(DynamicArray(other.array[length:]))
        return result

    def get_middle(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def index_of(self, val):
        for i in range(self.size):
            if self.array[i] == val:
                return i
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        other = DynamicArray(factor=self.factor)
        other.array = self.array[index:self.size]
        other.size = self.size - index
        self.size = index
        return other

    def resize_with_custom_factor(self, factor):
        self.factor = factor