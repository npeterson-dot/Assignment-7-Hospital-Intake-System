
class Patient:
    """Stores a patient's name and urgency level."""

    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    """Manages emergency patients using a min-heap."""

    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        # Move a patient up if they are more urgent than their parent.
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index], self.data[index]
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        # Move a patient down until the heap order is restored.
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if (left < len(self.data) and
                    self.data[left].urgency < self.data[smallest].urgency):
                smallest = left

            if (right < len(self.data) and
                    self.data[right].urgency < self.data[smallest].urgency):
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest], self.data[index]
            )
            index = smallest

    def insert(self, patient):
        # Add the patient, then restore the heap order.
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        # Return the most urgent patient without removing them.
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        # Handle an empty queue.
        if not self.data:
            return None

        # Handle a queue with only one patient.
        if len(self.data) == 1:
            return self.data.pop()

        # Move the last patient to the root and restore heap order.
        most_urgent = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return most_urgent


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()

    print("Testing an empty queue:")
    print("Peek:", heap.peek())
    print("Remove:", heap.remove_min())

    print("\nAdding patients:")
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    print("\nChecking the most urgent patient:")
    next_up = heap.peek()
    print(next_up.name, next_up.urgency)

    print("\nRemoving the most urgent patient:")
    served = heap.remove_min()
    print("Served:", served.name)
    heap.print_heap()

    print("\nTesting a single patient:")
    single_heap = MinHeap()
    single_heap.insert(Patient("Riley", 2))
    print("Served:", single_heap.remove_min().name)

    print("\nTesting multiple urgency levels:")
    test_heap = MinHeap()
    test_heap.insert(Patient("Morgan", 7))
    test_heap.insert(Patient("Dana", 4))
    test_heap.insert(Patient("Casey", 1))
    test_heap.insert(Patient("Alex", 6))
    test_heap.insert(Patient("Sam", 2))

    while test_heap.peek() is not None:
        patient = test_heap.remove_min()
        print(f"Served: {patient.name} ({patient.urgency})")
