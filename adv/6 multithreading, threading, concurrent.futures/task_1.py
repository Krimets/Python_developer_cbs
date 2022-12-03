# Завдання 1
# Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread, і заміряйте
# швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же набір завдань на
# ThreadPoolExecutor. Як приклади використовуйте останні значення, від мінімальних і до максимально можливих,
# щоб побачити приріст або втрату продуктивності.

import math
from concurrent.futures import ThreadPoolExecutor
import threading
import time


def handler():
    print('Value: ', math.factorial(1310))


task = threading.Thread(target=handler)
started_at = time.time()
print('Thread RESULT')
task.start()
task.join()
print('Time: {}'.format(time.time() - started_at))
print()


def run_by_executor(executor_class):
    executor = executor_class()
    started = time.time()
    future = executor.submit(handler)
    result = future.result()
    print('Time: {spent_time}'.format(spent_time=time.time() - started))


print('ThreadPoolExecutor RESULT')
run_by_executor(ThreadPoolExecutor)
