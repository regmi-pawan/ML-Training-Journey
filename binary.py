def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle element
        
        # Check if the target is at the mid
        if arr[mid] == target:
            return mid  # Return the index of the target element
        
        # If the target is smaller, ignore the right half
        elif arr[mid] > target:
            right = mid - 1
        
        # If the target is larger, ignore the left half
        else:
            left = mid + 1
    
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

        # Sort the array before applying Binary Search
        arr.sort()
        print(f"Sorted array: {arr}")
        
        target = int(input("Enter the element to search for: "))

        # Perform Binary Search
        result = binary_search(arr, target)

        if result != -1:
            print(f"Element {target} found at index {result}.")
        else:
            print(f"Element {target} not found in the array.")
except ValueError:
    print("Please enter valid integers.")
