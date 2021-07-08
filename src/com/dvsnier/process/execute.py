# -- coding:utf-8 --

import datetime
import logging
import subprocess
import time

from com.dvsnier.directory.common_dir import generate_complex_file_name


def execute(cmds, quiet=True):
    'the process execute that a command'
    content = ''
    stdouts = None
    start = time.time()
    p = subprocess.Popen(cmds[0], stdout=subprocess.PIPE, shell=True)
    # logging.debug('the current sub process pid(cwd: %s, ppid: %s, id: %s%d).' %
    #               (p.pid, os.getppid(), type(p), id(p)))
    processes = [p]
    for x in cmds[1:]:
        #
        # the airticle link reference:
        #
        # 1. https://docs.python.org/2.7/library/subprocess.html#subprocess.Popen.communicate
        # 2. https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate
        # 3. https://stackoverflow.com/questions/58649679/resourcewarning-unclosed-file-io-bufferedreader-name-4
        # 4. https://python.readthedocs.io/en/stable/library/subprocess.html
        #
        p = subprocess.Popen(x, stdin=p.stdout, stdout=subprocess.PIPE, bufsize=1024, shell=True)
        # logging.debug(
        #     'the current sub process pid(cwd: %s, ppid: %s, id: %s%d).' %
        #     (p.pid, os.getppid(), type(p), id(p)))
        # logging.debug(type(p), id(p))
        processes.append(p)
        # logging.debug('the current run process pid(cwd: %s, ppid: %s, id: %s%d).' %
        #               (p.pid, os.getppid(), type(p), id(p)))
        # logging.debug(type(p), id(p))
    stdouts, stderrs = p.communicate()
    if stderrs:
        logging.error(stderrs)
    for p in processes:
        p.wait()

    end = time.time()
    if not quiet:
        msg = '[%.5f] -> %s' % (end - start, ' | '.join(cmds))
        logging.debug(msg)
    if stdouts:
        if isinstance(stdouts, str):
            content = str(stdouts).rstrip('\n')
        elif isinstance(stdouts, bytes):
            content = str(stdouts.rstrip(bytes('\n', encoding='utf-8')), encoding='utf-8')
        else:
            content = ''
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
