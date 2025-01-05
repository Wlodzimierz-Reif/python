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

def merge_sort(arr):
    result = arr
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                result[k] = left_half[i]
                i += 1
            else:
                result[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            result[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            result[k] = right_half[j]
            j += 1
            k += 1
            
    return result
            
input_string = input('Enter a string: ')
split_input = list(input_string)

sorted = merge_sort(split_input)
print(f'Sorted: {sorted}')