# -*- coding:utf-8 -*-

import logging

from com.dvsnier.directory.common_dir import generate_complex_file_name


def config(kwargs):
    '''
        the logging config info:
            config(**kwargs={output_dir_name=\' \', file_name=\' \', level=logging.ERROR})
    '''
    if kwargs.get('output_dir_name') is None or len(kwargs.get('output_dir_name').strip()) == 0:
        raise KeyError('the current kwargs[output_dir_name] is empty.')
    if kwargs.get('file_name') is None or len(kwargs.get('file_name').strip()) == 0:
        raise KeyError('the current kwargs[file_name] is empty.')
    if kwargs.get('level') is not None and kwargs.get('level') < 0:
        raise KeyError('the current kwargs[level] is invalid.')
    else:
        kwargs['level'] = logging.ERROR
    file_name = generate_complex_file_name(kwargs['output_dir_name'], kwargs['file_name'])
    logging.basicConfig(
        filename=file_name,
        filemode='a',
        format='[%(asctime)s][%(levelname)8s] --- %(message)s',
        # format=
        # '[%(asctime)s][%(levelname)8s][%(filename)s:%(lineno)s] --- %(message)s',
        level=kwargs['level'])
    logging.info('this current file is %s' % (file_name))
    return logging
