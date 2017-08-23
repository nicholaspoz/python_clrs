class Heap:
    @staticmethod
    def left(index):
        return 2 * index

    @staticmethod
    def right(index):
        return (2 * index) + 1

    @staticmethod
    def parent(index):
        return index // 2

    def __init__(self, array):
        self._array = array

    def __getitem__(self, key):
        return self._array[key]

    def __setitem__(self, key, value):
        self._array[key] = value

    def __len__(self):
        return len(self._array)

    def max_heapify(self, index, heap_size):
        l = Heap.left(index)
        r = Heap.right(index)
        largest = index
        if l < heap_size and self[largest] < self[l]:
            largest = l
        if r < heap_size and self[largest] < self[r]:
            largest = r
        if largest != index:
            self[index], self[largest] = self[largest], self[index]
            self.max_heapify(largest, heap_size)

    def build_max_heap(self):
        for i in range((len(self) // 2), -1, -1):
            self.max_heapify(i, len(self))

    def heap_sort(self):
        self.build_max_heap()
        heap_size = len(self) - 1
        for index in range((len(self) - 1), 0, -1):
            self[index], self[0] = self[0], self[index]
            heap_size -= 1
            self.max_heapify(0, heap_size)
