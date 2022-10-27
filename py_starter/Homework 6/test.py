b = 0
s = []
s1 = []
while b != 10:
    b += 1
    t = int(input('Введiть число: '))
    s.append(t)
    s1.append(t ** 3)
print(s1)
my_list1 = s.copy()
my_list1.sort()
print(my_list1)
my_list1.sort(reverse=True)
print(my_list1)
