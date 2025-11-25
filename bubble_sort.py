# Direct translation of the C program

a = int(input("Enter the number of items in the array: "))
c = [0] * (a + 1)   # create array with dummy 0th element (1-indexed like C)

print("Enter the elements of the array:")
for i in range(1, a + 1):
    c[i] = int(input())

# Bubble-sort–like logic used in your code
for i in range(1, a + 1):
    for j in range(i, a + 1):
        if c[i] > c[j]:
            c[i], c[j] = c[j], c[i]

print("The bubble sort order is:")
for i in range(1, a + 1):
    print(c[i])
