import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    
    for h, count in hashes:
        print(h, count)


def pwnded_api_check(password):
    sha1hashword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1hashword[:5], sha1hashword[5:]
    res = request_api_data(first5_char)
    print(res)
    return get_password_leaks_count(res, tail)


print(pwnded_api_check("hi"))