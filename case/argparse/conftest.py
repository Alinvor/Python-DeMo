# -*- coding:utf-8 -*-

import logging
import os
import shutil
import tempfile

from com.dvsnier.config.journal.common_config import config
import pytest

kwargs = {'output_dir_name': 'pytest', 'file_name': 'log', 'level': logging.DEBUG}
config(kwargs)


@pytest.fixture(scope="session")
def _temp_dir():
    ''' _temp_dir '''
    temp = tempfile.mkdtemp(prefix='argprase-')
    print('\n')
    logging.debug('the current temp dir is {}'.format(temp))
    yield temp
    shutil.rmtree(temp)


@pytest.fixture(scope="session")
def _temp_file():
    ''' _temp_file '''
    fd, temp = tempfile.mkstemp(prefix='argprase-', suffix='.tmp')
    # print('\n')
    logging.debug('the current temp path is {}'.format(temp))
    yield temp
    os.remove(temp)
