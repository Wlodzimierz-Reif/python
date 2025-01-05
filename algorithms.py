# BIG O NOTATION
# Time Complexity: How many operations are performed as the size of the input grows
# Constant Time: O(1)
# Logarithmic Time: O(log n)
# Linear Time: O(n)
# Quadratic Time: O(n^2)
# Polynomial Time: O(n^c)
# Exponential Time: O(c^n)

# LINEAR SEARCH
# Time Complexity: O(n)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# ORDERED LINEAR SEARCH
# Time Complexity: O(n)
# List must be sorted beforehand
# Implement a break if the current element is greater than the target

# BINARY LINEAR SEARCH
# Time Complexity: O(log n)
# List must be sorted beforehand
# Divide the list in a half and compare the target with the middle element
# If the target is greater than the middle element, search the right half
# If the target is less than the middle element, search the left half
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char = input('Enter a character: ')
first = 0
last = len(al) - 1
found = False
mid = 0
while first <= last and not found:
    mid = (first + last) // 2
    if char == al[mid]:
        found = True
        break
    else:
        if char > al[mid]:
            first = mid + 1
        else:
            last = mid - 1
print(f'Character {"" if found else "not "}found in the list {f"at position {mid}" if found else ""}')