# Завдання 6
# Використовуючи сервіс https://jsonplaceholder.typicode.com/, спробуйте побудувати різні типи запитів та обробити
# відповіді. Необхідно попрактикуватися з urllib та бібліотекою requests. Рекомендується спочатку спробувати виконати
# запити, використовуючи urllib, а потім спробувати реалізувати те саме, використовуючи requests.

from urllib import request, parse

response = request.urlopen('https://jsonplaceholder.typicode.com/')

print(response.code)  # 200
print(response.getcode())  # 200
print(response.status)  # 200

print(response.msg)  # OK
print(response.reason)  # OK

print(response.headers)
print(1)
print(response.getheaders())
print(2)
print(response.getheader('Connection'))  # close
print(response.headers.get('Connection'))  # close
print(response.length)  # None. From wikipedia.org 75135 bytes
print(3)
print(response.peek())  # returns the part of the response
print(4)
print(response.isclosed())  # False

data = response.read()
print(type(data))  # class 'bytes'>

print(response.isclosed())  # True -- connection closes after reading of the response

utf_8 = data.decode('utf-8')  # to convert the data from response from bytes into utf-8
print(type(utf_8))  # <class 'str'>

print()

# https://www.youtube.com/watch?v=LosIGgon_KM&ab_channel=Socratica
params = {"v": "LosIGgon_KM", "ab_channel": "Socratica"}
querystring = parse.urlencode(params)
url = 'https://www.youtube.com/watch' + '?' + querystring
print(url)
response = request.urlopen(url)
print(response.isclosed())  # False
print(response.code)  # 200
html = response.read().decode('utf-8')
print(html[:501])
print(response.isclosed())  # True

# https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer
params = {"v": "ng2o98k983k", "ab_channel": "CoreySchafer"}
querystring = parse.urlencode(params)
url = 'https://www.youtube.com/watch' + '?' + querystring
print(url)
response = request.urlopen(url)
print(response.code)
print(response.headers)
html = response.read().decode('utf-8')
print(html[:300])