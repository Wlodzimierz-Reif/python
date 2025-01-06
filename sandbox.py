def insertion_sort(input_list):
    list = input_list
    n = len(list)
    for i in range(n):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
    return list

print(insertion_sort(["3", "5", "9", "6", "8", "4", "3", "2", "1"]))

i = 2
j = 1