#
# Max-Heapify function to maintain the max-heap property.
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# Build a max-heap from the array.
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


# Heap Sort function.
def heap_sort(arr):
    n = len(arr)
    # Build a max-heap from the array.
    build_max_heap(arr)

    # Starting with the root (the maximum element), the algorithm places the maximum element into the correct place in the array by swapping it with the element in the last position in the array.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
       # Condition 3: Discard this last node (knowing that it is in its correct place) by decreasing the heap size, and calling MAX-HEAPIFY on the new (possibly incorrectly-placed) root.
        max_heapify(arr, i, 0)
    return arr
class minPriorityQueue:
    def __init__(self):
        # Initialize the minPriorityQueue with an empty heap.
        self.heap = []

    def insert(self, value):
        # Insert an element with a specified priority value into the priority queue.
        self.heap.append(value)
        self.percolate_up(len(self.heap) - 1)  # Ensure the heap property is maintained.

    def first(self):
        # Return the element with the lowest/minimum priority value, i.e., the root of the heap.
        if len(self.heap) == 0:
            raise IndexError("Priority queue is empty")
        return self.heap[0]

    def remove_first(self):
        # Remove and return the element with the lowest/minimum priority value.
        if len(self.heap) == 0:
            raise IndexError("Priority queue is empty")
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]  # The minimum value to be removed.
        last = self.heap.pop()  # Get the last element in the heap.
        self.heap[0] = last  # Replace the root with the last element.
        self.percolate_down(0)  # Ensure the heap property is maintained.
        return min_val

    def percolate_up(self, i):
        # Restore the heap property by moving an element up the heap.
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def percolate_down(self, i):
        # Restore the heap property by moving an element down the heap.
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if (left < len(self.heap) and self.heap[left] < self.heap[smallest]):
                smallest = left

            if (right < len(self.heap) and self.heap[right] < self.heap[smallest]):
                smallest = right

            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break


if __name__ == '__main__':
    arr = [12]

    # Call Heap Sort and print the sorted array.
    sorted_arr = heap_sort(arr)
    print(sorted_arr)

    pq = minPriorityQueue()
    pq.insert(5)
    pq.insert(3)
    pq.insert(7)
    pq.insert(1)
    pq.insert(0)

    print(pq.first())          # Should print the element with the lowest priority (0).
    print(pq.remove_first())   # Should remove and print the lowest priority element (0).
    print(pq.first())          # Should print the new element with the lowest priority (1).