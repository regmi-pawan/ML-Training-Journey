def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root, swap and continue heapifying the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap (rearrange the array to satisfy the heap property)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)  # Call heapify on the reduced heap

    return arr


# Get user input for array size and values
try:
    size = int(input("Enter the size of the array: "))
    if size <= 0:
        print("Array size must be greater than 0.")
    else:
        arr = []
        for i in range(size):
            value = int(input(f"Enter value {i + 1}: "))
            arr.append(value)

        print("Original array:", arr)
        sorted_arr = heap_sort(arr)
        print("Sorted array:", sorted_arr)
except ValueError:
    print("Please enter valid integers.")
