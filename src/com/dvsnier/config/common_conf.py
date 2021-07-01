# -*- coding:utf-8 -*-

import logging

from com.dvsnier.directory.common_dir import generate_complex_file_name


def logging_conf(kwargs):
    '''
        the logging conf info:
            logging_conf(**kwargs={output_dir_name=\' \', file_name=\' \', level=logging.DEBUG})
    '''
    if kwargs.get('output_dir_name') is None or len(kwargs.get('output_dir_name')) == 0:
        raise KeyError('the current kwargs[output_dir_name] is empty.')
    if kwargs.get('file_name') is None or len(kwargs.get('file_name')) == 0:
        raise KeyError('the current kwargs[file_name] is empty.')
    if kwargs.get('level') < 0:
        raise KeyError('the current kwargs[level] is invalid.')
    file_name = generate_complex_file_name(kwargs['output_dir_name'], kwargs['file_name'])
    logging.basicConfig(
        filename=file_name,
        filemode='a',
        format='[%(asctime)s][%(levelname)8s] --- %(message)s',
        # format=
        # '[%(asctime)s][%(levelname)8s][%(filename)s:%(lineno)s] --- %(message)s',
        level=kwargs['level'])
    logging.info('this current file is %s' % (file_name))
