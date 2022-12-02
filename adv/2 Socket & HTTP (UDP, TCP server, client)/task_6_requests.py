# Завдання 6
# Використовуючи сервіс https://jsonplaceholder.typicode.com/, спробуйте побудувати різні типи запитів та обробити
# відповіді. Необхідно попрактикуватися з urllib та бібліотекою requests. Рекомендується спочатку спробувати виконати
# запити, використовуючи urllib, а потім спробувати реалізувати те саме, використовуючи requests.

import requests

img = requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png', 'wb') as image:
    image.write(img.content)  # content returns data in bytes. Good for non-text data


response = requests.get('https://jsonplaceholder.typicode.com/')  # analog of urlopen => .read()
print(response.text)  # returns the html of file
print(response.status_code)  # 200 -- analog to urlopen => .code
print(response.ok)  # True if OK. False if not
print(response.headers)  # returns list of headers. Same as in urllib

print("=" * 50)
print("GET via requests")
querystring = {'page': 2, 'count': 25}
# request data from https://httpbin.org/get?page=2&count=25
response = requests.get('https://httpbin.org/get', params=querystring)
print(response.url)  # returns url
print("=" * 100)
print(response.text)  # reads text from response

print("=" * 50)
print("POST via requests. In PUT same as in POST. Just post to be changed to put")
payload = {'username': 'hell_yeah', 'password': 'blablabla'}
# sending data to https://httpbin.org/
response = requests.post('https://httpbin.org/post', data=payload)
print(response.text)  # return the data, rcvd from the url after posting
response_jsn = response.json()  # the data may be saved in json format, which is a dict per se. Same as json.loads()
print(response_jsn)
print(response_jsn['form'])  # {'password': 'blablabla', 'username': 'hell_yeah'}

print("=" * 50)
print("Use of GET for authentication")

response = requests.get('https://httpbin.org/basic-auth/hell/yeah', auth=('hell', 'yeah'))
'''Tuple must match with attributes of auth request, i.e. {user}/{password}'''
print(response)  # <Response [200]>
print(response.text)
'''{
  "authenticated": true, 
  "user": "hell"
}
'''
response = requests.get('https://httpbin.org/basic-auth/hell/yeah', auth=('hell', 'no'))
print(response)  # <Response [401]>  -- Unauthorised. auth doesn't match with path 'basic-auth/hell/yeah'

print("=" * 50)
print("Check of timeout operation")
response = requests.get('https://httpbin.org/delay/1', timeout=3)  # timeout 3 sec, site will respond in 1 sec. OK.
print(response)  # <Response [200]>

response = requests.get('https://httpbin.org/delay/6', timeout=3)  # timeout 3 sec, site will respond in 6 sec. Not OK
print(response)  # ConnectTimeout
