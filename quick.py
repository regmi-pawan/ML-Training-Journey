def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choosing a pivot (Here we are choosing the last element as pivot)
    pivot = arr[-1]

    # Partitioning the array into two sub-arrays: 
    # one with elements smaller than the pivot, and the other with elements larger than the pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort the left and right sub-arrays and combine with the pivot in between
    return quick_sort(left) + [pivot] + quick_sort(right)


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
        sorted_arr = quick_sort(arr)
        print("Sorted array:", sorted_arr)
except ValueError:
    print("Please enter valid integers.")
