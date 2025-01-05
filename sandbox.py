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