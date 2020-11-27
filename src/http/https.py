# coding:utf-8

import urllib2
import logging
from conf.common_conf import logging_conf


class Request(object):
    'the request class'

    def __init__(self):
        super(Request, self).__init__()

    def requests(self, req_url):
        'the request address'
        logging.info('this request url is %s' % req_url)
        response = urllib2.urlopen(req_url)
        headers = response.headers
        if any(headers):
            logging.debug('this request headers is %s' % str(headers.dict))

        response_to_string = str(response.read())
        logging.debug('this is response is %s' % response_to_string)
        return response


if __name__ == "__main__":
    logging_conf()
    request = Request()
    url = 'https://www.zhihu.com/hot'
    response = request.requests(url)
