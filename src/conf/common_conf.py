# -*- coding:utf-8 -*-

import logging
from dir.common_dir import generate_complex_file_name


def logging_conf():
    'the logging conf info'
    file_name = generate_complex_file_name('http', 'http')
    logging.basicConfig(
        filename=file_name,
        filemode='a',
        format='[%(asctime)s][%(levelname)8s] --- %(message)s',
        # format=
        # '[%(asctime)s][%(levelname)8s][%(filename)s:%(lineno)s] --- %(message)s',
        level=logging.DEBUG)
    logging.info('this current file is %s' % (file_name))
