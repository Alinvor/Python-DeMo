# -- coding:utf-8 --

import datetime
# import logging
import os
import platform
import time
import sys
import subprocess

from com.dvsnier.directory.common_dir import generate_complex_file_name


def execute(cmds, quiet=True):
    'the process execute that a command'
    start = time.time()
    p = subprocess.Popen(cmds[0], stdout=subprocess.PIPE, shell=True)
    # logging.debug('the current sub process pid(cwd: %s, ppid: %s, id: %s%d).' %
    #               (p.pid, os.getppid(), type(p), id(p)))
    processes = [p]
    for x in cmds[1:]:
        p = subprocess.Popen(x, stdin=p.stdout, stdout=subprocess.PIPE, shell=True)
        # logging.debug(
        #     'the current sub process pid(cwd: %s, ppid: %s, id: %s%d).' %
        #     (p.pid, os.getppid(), type(p), id(p)))
        # logging.debug(type(p), id(p))
        processes.append(p)
    # logging.debug('the current run process pid(cwd: %s, ppid: %s, id: %s%d).' %
    #               (p.pid, os.getppid(), type(p), id(p)))
    # logging.debug(type(p), id(p))
    output = p.communicate()[0]
    for p in processes:
        p.wait()

    end = time.time()
    if not quiet:
        if platform.system() == 'Linux' and os.isatty(1):
            print('\r'),
        msg = '[%.5f] -> %s' % (end - start, ' | '.join(cmds))
        print(msg)
    content = ''
    if sys.version_info.major > 2:
        content = str(output.rstrip(bytes('\n', encoding='utf-8')))
    else:
        content = output.rstrip('\n')
    # logging.debug('the current run process pid(cwd: %s, ppid: %s, id: %s%d).' %
    #               (p.pid, os.getppid(), type(p), id(p)))
    return content


def trace(cmds):
    'the process trace that a command and print level command'
    if cmds:
        command = []
        for cmd in cmds:
            command.append(cmd)
            file_name = generate_complex_file_name('trace', 'trace')
            with open(file_name, 'a+') as file:
                if cmd is not cmds[0]:
                    file.write('\n')
                file.write(
                    str('the current timestamp: {timestamp}\n'.format(
                        timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))))
                file.write(str('the current command: [{cmd}].\n'.format(cmd=' | '.join(command))))
                # file.write(execute(command, quiet=False))
                file.write(execute(command, quiet=True))
                file.write('\n')
