# Завдання 3
# Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор, який залишатиме в
# послідовності лише парні числа.

def check_if_even(fn):
    print("Decorator function \"if_even\" has started.")

    def wrapper_func(n):
        lst = []
        [lst.append(i) for i in fn(n) if i % 2 == 0 and i != 0]
        return lst

    return wrapper_func


@check_if_even
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(fib(30))
