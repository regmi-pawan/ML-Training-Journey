def insertion_sort(arr):
    # Traverse through the array from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted in the sorted part of the array
        j = i - 1  # Index of the last element in the sorted part

        # Shift elements of arr[0..i-1] that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at the correct position
        arr[j + 1] = key

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
        sorted_arr = insertion_sort(arr)
        print("Sorted array:", sorted_arr)
except ValueError:
    print("Please enter valid integers.")
