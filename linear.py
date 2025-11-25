def linear_search(arr, target):
    # Traverse the array and check each element
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index of the target element
    return -1  # Return -1 if target is not found

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

        target = int(input("Enter the element to search for: "))

        # Perform Linear Search
        result = linear_search(arr, target)

        if result != -1:
            print(f"Element {target} found at index {result}.")
        else:
            print(f"Element {target} not found in the array.")
except ValueError:
    print("Please enter valid integers.")
