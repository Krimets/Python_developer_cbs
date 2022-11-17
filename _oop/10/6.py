import copy

aList = [1,2]
bList = [3,4]

kvps = {'1' : aList, '2':bList}
theCopy = copy.deepcopy(kvps)

kvps['1'][0] = 5

sum = kvps['1'][0] + theCopy['1'][0]
print(sum)


def d(p1, **p2):
    print(type(p2))
d('capitals', Arizona='Phoenix',
                    California='Sacramento',
        Texas='Austin')

def my(x,y,z,a):
    print(x+y)

nums = [1,2,3,4]
my(*nums)

counter = 1
def do():
    global counter
    for i in (1,2,3):
        counter += 1
do()
print(counter)

x = True
y = False
z = False

# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

if x or y and z:
    print('y')


names1 =['Amir']
if 'amir' in names1:
    print(1)
loc = names1.index("Edward")
print(loc)
a = [1,2,3,None,(),[],]
print(len(a))
