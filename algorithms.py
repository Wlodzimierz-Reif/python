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
# al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# char = input('Enter a character: ')
# first = 0
# last = len(al) - 1
# found = False
# mid = 0
# while first <= last and not found:
#     mid = (first + last) // 2
#     if char == al[mid]:
#         found = True
#         break
#     else:
#         if char > al[mid]:
#             first = mid + 1
#         else:
#             last = mid - 1
# print(f'Character {"" if found else "not "}found in the list {f"at position {mid}" if found else ""}')


# ###################
# SIMPLE SORT
# Big-O Notation: O(n^2)
# str_input = input('Enter a string: ')
# min = 0
# sorted_str = []
# str = list(str_input)
# for i in range(len(str)):
#     min = str[0]
#     for j in range(len(str)):
#         if str[j] < min:
#             min = str[j]
#     sorted_str.append(min)
#     str.remove(min)
# print(sorted_str)

# BUBBLE SORT
# Big-O Notation: O(n^2) but faster than simple sort
# str_input = input("Enter a string: ")
# n = len(str_input)
# sorted_str = []
# str = list(str_input)
# hasSwapped = False
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if str[j] > str[j + 1]:
#             str[j], str[j + 1] = str[j + 1], str[j]
#             hasSwapped = True
# print(', '.join(str)) # joining th list

# MERGE SORT
def merge_sort(arr):
    result = []
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i, j, k, = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            arr[k] = left_half[1]
            i, k += 1
            
        while j < len(right_half):
            arr[k] = right_half[j]
            j, k += 1
            
input_string = input('Enter a string: ')
split_input = input_string.split()
print(split_input)
print(type(split_input))
# numbers = [int(n) for n in split_input]

merge_sort(split_input)
print(f'Sorted: {split_input}')