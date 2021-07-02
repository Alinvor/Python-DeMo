# -*- coding:utf-8 -*-

from com.dvsnier.config.common_config import config
from deprecated import deprecated


@deprecated(version='0.0.2.dev1',
            reason="You should use the from com.dvsnier.config.common_config import config method, that We will delete \
this method after extending 2-3 versions")
def logging_conf(kwargs):
    '''
        the logging conf info:
            logging_conf(**kwargs={output_dir_name=\' \', file_name=\' \', level=logging.ERROR})
    '''
    return config(kwargs)
