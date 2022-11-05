def generator():
    count = 0
    while count in range(3):
        yield count
        count += 1

g = generator()
for i in g:
    print(i)
for i in g:
    print(i)
