# Завдання 8
# Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу та словник як передавальні дані
# (опціональний). Виконувати запит з отриманим методом на отриманий ресурс, передаючи дані відповідним методом, та
# друкувати на консоль статус-код, заголовки та тіло відповіді.

import requests


def data_output(data):
    print(f"STATUS CODE:\n{data.status_code}\n")
    print(f"HEADERS:\n{data.headers}\n")
    print(f"BODY: \n{data.text}\n")


def call(url, method, dictionary=None):
    if method == 'GET' and not dictionary:
        result = requests.get(url)
        data_output(result)
    elif method == 'GET' and dictionary:
        result = requests.get(url, params=dictionary)
        data_output(result)
    elif method == 'HEAD' and not dictionary:
        result = requests.head(url)
        print(f"STATUS CODE:\n{result.status_code}\n")
        print(f"HEADERS:\n{result.headers}\n")
    elif method == 'HEAD' and dictionary:
        result = requests.head(url, params=dictionary)
        print(f"STATUS CODE:\n{result.status_code}\n")
        print(f"HEADERS:\n{result.headers}\n")
    elif method == 'POST' and dictionary:
        result = requests.post(url, data=dictionary)
        data_output(result)
    elif method == 'PUT' and dictionary:
        result = requests.post(url, data=dictionary)
        data_output(result)
    else:
        print("Wrong method!")
        exit(1)

# call('https://www.example.com/', 'POST', {"name": "Ecce", "surname": "Homo"})
#
# call('https://www.example.com/', 'GET')
#
# call('https://www.example.com/', 'GET', {"name": "Ecce", "surname": "Homo"})
#
# call('https://www.example.com/', 'PUT', {"name": "Ecce", "surname": "Homo"})
#
# call('https://httpbin.org/', 'HEAD')
#
# call('https://httpbin.org/', 'HEAD', {"name": "Ecce", "surname": "Homo"})


def interact():
    url = input("URL: \n")
    method = input("HTTP method: \n").upper()
    dictionary = input("Dictionary of data (for POST or PUT -- compulsory)\n"
                       "or dictionary of URL parameters (for GET and HEAD -- optionally): \n")
    return call(url, method, dictionary)


interact()
