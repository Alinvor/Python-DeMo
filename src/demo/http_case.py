# -*- coding:utf-8 -*-

from com.dvsnier.http.https import Request
from com.dvsnier.dir.common_dir import generate_complex_file_name

_request = None


def run(url):
    return _request.requests(url)


if __name__ == "__main__":
    _request = Request()
    url = 'http://www.xuexi.la/sudu/523441.html'
    # url = 'https://www.thepaper.cn/newsDetail_forward_9864719'
    response = run(url)
    response_file = generate_complex_file_name('request', 'response')
    with open(response_file, 'w+') as f:
        f.write(str(response.read()))
