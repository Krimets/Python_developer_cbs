# Завдання 4
# Створіть звичайну функцію множення двох чисел. Створіть каррувану функцію множення двох чисел. Частково застосуйте
# її до одного аргументу, до двох аргументiв

def func(a, b):
    return a * b


def currying_func(a):
    def fig(b):
        return a * b
    return fig


print(currying_func(2)(3))

arg = currying_func(2)
print(arg(3))
