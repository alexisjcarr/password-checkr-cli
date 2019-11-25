import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again.')
    return res


def pwnded_api_check(password):
    sha1hashword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1hashword


print(pwnded_api_check("hi"))