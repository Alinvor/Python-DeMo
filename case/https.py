# coding:utf-8

# import urllib
import urllib2
import os
# import shutil
import logging
import time


def requests():

    req_url = 'http://www.baidu.com/'
    # print(req_url)
    logging.info('this request url is %s' % req_url)
    response = urllib2.urlopen(req_url)
    headers = response.headers

    root_dir = os.path.dirname(os.path.abspath('.'))
    project_dir = os.path.abspath('.')
    src_dir = os.path.join(project_dir, 'src')
    out_dir = os.path.join(project_dir, 'out')
    req_dir = os.path.join(out_dir, 'request')
    log_file_name = 'runtime.log'
    log_file = os.path.join(req_dir, log_file_name)

    if os.path.exists(req_dir):
        removeTree(req_dir)
    else:
        os.makedirs(req_dir)

    with open(log_file, 'w+') as f:
        f.write('root_dir: ' + root_dir)
        f.write('\n')
        f.write('project_dir: ' + project_dir)
        f.write('\n')
        f.write('src_dir: ' + src_dir)
        f.write('\n')
        f.write('out_dir: ' + out_dir)
        f.write('\n')
        f.write('\n')
        f.write('req_dir: ' + req_dir)
        f.write('\n')
        f.write('log_file: ' + log_file)
        f.write('\n')

    if any(headers):
        header_of_log = os.path.join(req_dir, 'response.header.log')
        file = open(header_of_log, 'w')
        value = str(headers.dict)
        logging.debug('this request headers is %s' % value)
        file.write(value)
        file.close()

    body_of_log = os.path.join('out/request', 'response.body.log')
    file = open(body_of_log, 'w')
    response_to_string = str(response.read())
    # logging.debug('this is response is %s' % response_to_string)
    #
    # logging.debug('this is debug message.')
    # logging.info('this is info message.')
    # logging.warning('this is warning message.')
    # logging.error('this is error message.')
    # logging.critical('this is critical message.')
    file.write(response_to_string)
    file.close()


def removeTree(dir):
    # shutil.rmtree(req_dir)
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def generateFileName():
    'the generate out file name'
    project_dir = os.path.abspath('.')
    out_dir = os.path.join(project_dir, 'out')
    http_dir = os.path.join(out_dir, 'http')
    if not os.path.exists(http_dir):
        os.makedirs(http_dir)
    file_name = 'http_%s.log' % int(time.time())
    return os.path.join(http_dir, file_name)


if __name__ == "__main__":
    logging.basicConfig(
        filename=generateFileName(),
        filemode='a',
        format='[%(asctime)s][%(levelname)8s] --- %(message)s',
        # format=
        # '[%(asctime)s][%(levelname)8s][%(filename)s:%(lineno)s] --- %(message)s',
        level=logging.DEBUG)
    requests()
