# Implementation of max heap
# Assume each element has distinct key, and all parameters are used appropriately

def is_max_heap(arr, arr_size, root_index):
    if root_index >= arr_size:
        return True
    else:
        lc = 2 * root_index + 1
        rc = 2 * root_index + 2

        if lc < arr_size and arr[lc] > arr[root_index]:
            return False
        if rc < arr_size and arr[rc] > arr[root_index]:
            return False
        return is_max_heap(arr, arr_size, lc) and is_max_heap(arr, arr_size, rc)


class MaxHeap:
    def __init__(self, arr):
        self.__max_heap = arr
        self.__heap_size = len(arr)
        self.build_max_heap()

    def __getitem__(self, index):
        return self.__max_heap[index]

    def __len__(self):
        return len(self.__max_heap)

    def __get_left_child(self, root_index):
        """ Return the left child index given the root index """
        return 2 * root_index + 1

    def __get_right_child(self, root_index):
        """ Return the right child index given the root index """
        return 2 * root_index + 2

    def __get_parent(self, root_index):
        """ Return the parent index given the root index """
        return (root_index - 1) // 2

    def get_heap_size(self):
        return self.__heap_size

    def max_heapify(self, root_index, heap_size):
        """ Change an almost max heap into a max heap """
        lc = self.__get_left_child(root_index)
        rc = self.__get_right_child(root_index)
        max_index = root_index

        if lc < heap_size and self.__max_heap[lc] > self.__max_heap[max_index]:
            max_index = lc
        if rc < heap_size and self.__max_heap[rc] > self.__max_heap[max_index]:
            max_index = rc
        if max_index != root_index:
            self.__max_heap[root_index], self.__max_heap[max_index] = self.__max_heap[max_index], self.__max_heap[root_index]
            self.max_heapify(max_index, heap_size)

    def build_max_heap(self):
        """ Build a heap from a random arr """
        for root_index in range(self.__get_parent(self.__heap_size-1), -1, -1):
            self.max_heapify(root_index, self.__heap_size)

    def heap_sort(self):
        """ Sort into non-decreasing order """
        self.build_max_heap()
        for i in range(self.__heap_size-1, 0, -1):
            self.__max_heap[0], self.__max_heap[i] = self.__max_heap[i], self.__max_heap[0]
            self.max_heapify(0, i)

    def is_empty(self):
        return self.__heap_size == 0

    def is_in_heap(self, target):
        """ Return True if target is in the heap, or False otherwise """
        for item in self.__max_heap:
            if item == target:
                return True
        return False

    def find_max(self):
        """ Return the max element in the heap """
        if self.is_empty():
            return None
        else:
            return self.__max_heap[0]

    def extract_max(self):
        """ Return and remove the max element from the heap """
        if self.is_empty():
            return None
        else:
            self.__max_heap[0], self.__max_heap[self.__heap_size-1] = self.__max_heap[self.__heap_size-1], self.__max_heap[0]
            removed = self.__max_heap.pop()
            self.__heap_size -= 1
            self.max_heapify(0, self.__heap_size)
            return removed

    def insert(self, new):
        """ Insert the new data into an appropriate position s.t. the max heap structure is maintained """
        pass

    def delete(self, target):
        """ Delete target from the heap (if it exists) and maintain the max heap structure """
        pass

    def __str__(self):
        pass


