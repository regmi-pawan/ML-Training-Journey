def merge_sort(arr):
    # Base case: if the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    # Merge the two arrays by comparing the smallest elements of each
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If there are remaining elements in either half, add them to the result
    result.extend(left[i:])
    result.extend(right[j:])

    return result


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
        sorted_arr = merge_sort(arr)
        print("Sorted array:", sorted_arr)
except ValueError:
    print("Please enter valid integers.")
