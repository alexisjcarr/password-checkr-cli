import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, check the API and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())

    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwnded_api_check(password):
    sha1hashword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1hashword[:5], sha1hashword[5:]
    res = request_api_data(first5_char)

    return get_password_leaks_count(res, tail)


def main(args):
    for password in args:
        count = pwnded_api_check(password)

        if count:
            print(f'\n{password} was found {count} times... you should probably change your password')
        else:
            print(f'\n{password} was not found. carry on')
    
    return '\ncheck completed\n'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
