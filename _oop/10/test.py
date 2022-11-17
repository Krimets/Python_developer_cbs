class Acc:
    def __init__(self, id):
        self.id = id
        id = 66


instance = Acc(123)
print(instance.id)


c = {}
c[1] = 1
c['1'] = 2
c[1.0] = 4

sum = 0
for k in c:
    sum += c[k]

print(sum)

ccc = {}

def addone(country):
    if country in ccc:
        ccc[country] += 1
    else:
        ccc[country] = 1
addone('China')
addone('Japan')
addone('china')

print(len(ccc))