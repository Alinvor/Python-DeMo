# -*- coding:utf-8 -*-

import logging
import os
import subprocess
import pytest
import sys


def test_cmd_1(execute):
    ''' the test cmd '''
    print('\n  the test_cmd_1 ended.')
    logging.info('the test_cmd_1 ended.')


IS_DEBUG_ONLY = False
# IS_SKIP = True


@pytest.fixture(scope='session', autouse=True)
def generic_cmd_env(_temp_dir, _temp_file):
    ''' generic cmd env '''
    pass


# @pytest.fixture(scope='session', params=['test_argparse_0.py'])
# @pytest.fixture(scope='session', params=['test_argparse_1.py'])
# @pytest.fixture(scope='session', params=['test_argparse_2.py'])
@pytest.fixture(scope='session',
                params=[
                    pytest.param('test_argparse_0.py', marks=pytest.mark.skip),
                    pytest.param('test_argparse_1.py', marks=pytest.mark.skip), 'test_argparse_2.py'
                ])
# @pytest.mark.parametrize('script_name', ['test_argparse_0.py', 'test_argparse_1.py', 'test_argparse_2.py'])
def generic_cmd_prefix(request):
    ''' the generic command prefix '''
    dest_script_name = os.path.join(os.path.dirname(__file__), request.param)
    logging.debug('the generic_cmd_prefix dest_script_name is {}'.format(dest_script_name))
    return [sys.executable, dest_script_name]


# the test_argparse_2.py script only
PARAMS_ARGPARSE_2 = [['-h'], ['./a', './b'], ['./a', './b', '-vs'], ['./a', './b', '-v1', '0'],
                     ['./a', './b', '-v1', '1'], ['./a', './b', '-v1', '2'], ['./a', './b', '-v2'],
                     ['./a', './b', '-v2', '-v2'], ['./a', './b', '-v'], ['./a', './b', '-q'],
                     ['./a', './b', '-vs', '-v1', '0'], ['./a', './b', '-vs', '-v1', '1'],
                     ['./a', './b', '-vs', '-v1', '2'], ['./a', './b', '-vs', '-v1', '0', '-v2'],
                     ['./a', './b', '-vs', '-v1', '1', '-v2'], ['./a', './b', '-vs', '-v1', '2', '-v2'],
                     ['./a', './b', '-vs', '-v1', '0', '-v2', '-v2'], ['./a', './b', '-vs', '-v1', '1', '-v2', '-v2'],
                     ['./a', './b', '-vs', '-v1', '2', '-v2', '-v2'], ['./a', './b', '-vs', '-v1', '0', '-v2', '-v'],
                     ['./a', './b', '-vs', '-v1', '1', '-v2', '-v'], ['./a', './b', '-vs', '-v1', '2', '-v2', '-v'],
                     ['./a', './b', '-vs', '-v1', '0', '-v2', '-q'], ['./a', './b', '-vs', '-v1', '1', '-v2', '-q'],
                     ['./a', './b', '-vs', '-v1', '2', '-v2', '-q']]


@pytest.fixture(params=PARAMS_ARGPARSE_2)
def generic_cmd_args(generic_cmd_prefix, request):
    ''' the generic command args '''
    dest_script_args = generic_cmd_prefix + request.param
    logging.debug('the current generic_cmd_args dest_script_args: {}'.format(dest_script_args))
    return dest_script_args


@pytest.fixture()
def execute(generic_cmd_args):
    ''' the execute '''
    try:
        args = generic_cmd_args
        if args:
            logging.warning('the parameters required for current execution, the command script: [\"{}\"]'.format(
                ' '.join(args)))
            if IS_DEBUG_ONLY:
                pass
            else:
                std_output = subprocess.check_output(args)
                if type(std_output) == bytes:
                    # logging.warning(str(std_output, encoding='utf-8'))
                    logging.info('the capture std output from subprocess:\n {}'.format(str(std_output,
                                                                                           encoding='utf-8')))
                else:
                    logging.warning(std_output)
                retcode = subprocess.check_call(args)
                if retcode == 0:
                    logging.info('the script verify passed.')
        else:
            logging.warning('the error script command line that is skipped.')
    finally:
        logging.debug('the execute ended')


if __name__ == "__main__":
    ''' the main point '''
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
