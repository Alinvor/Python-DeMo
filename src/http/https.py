# -*- coding:utf-8 -*-

from conf.common_conf import logging_conf
import urllib2
import logging


class Request(object):
    'the request class'

    _url = None  # the request url address

    # def __init__(self):
    #     super(Request, self).__init__()
    #     kwargs = {'output_dir_name': 'request', 'file_name': 'request'}
    #     logging_conf(kwargs)

    def __init__(self, *url):
        super(Request, self).__init__()
        self._url = url
        kwargs = {'output_dir_name': 'request', 'file_name': 'request'}
        logging_conf(kwargs)

    def requests(self, *req_url):
        'the request address'
        if len(req_url) == 0 or req_url is None:
            req_url = self._url
        if len(req_url) == 0:
            return
        logging.info('this request url is %s' % req_url)
        response = urllib2.urlopen(req_url[0])
        headers = response.headers
        if any(headers):
            logging.debug('this request headers is %s' % str(headers.dict))

        # response_to_string = str(response.read())
        # logging.debug('this is response is %s' % response_to_string)
        return response

    def getUrl(self):
        'the get url'
        if not len(self._url) == 0:
            logging.info('the current url is %s' % self._url)
        else:
            logging.info('the current url is empty')
        return self._url
