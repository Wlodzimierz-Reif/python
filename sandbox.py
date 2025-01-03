# file = open('test.txt', 'r')
# doc = file.readlines()
# lines = 0
# words = 0
# characters = 0
# for line in range(len(doc)):
#     lines += 1
#     print(line)
#     for word in doc[line].split(" "):
#         words += 1
#         characters += len(word)
# writefile = open('writefile.txt', 'w')
# writefile.write(f"Lines: {lines}\nWords: {words}\nCharacters: {characters}")

cities = dict([(1, "Edinburgh"), (2, "London"), (3, "Boston"), (4, "Tokyo")])

print(cities)
