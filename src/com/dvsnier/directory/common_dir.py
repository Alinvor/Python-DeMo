# -*- coding:utf-8 -*-

import datetime
# import logging
import os
import time

from deprecated import deprecated


@deprecated(
    version='0.0.2.dev1',
    reason="You should use the from com.dvsnier.directory.common_directory import CommonDirectory, that We will delete \
this method after extending 2-3 versions")
def generate_complex_file_name(output_dir_name, file_name):
    'the generate complex file name'
    output_dir = mk_output_dir(output_dir_name)
    name = str("%s_%s.log" % (file_name, int(time.time())))
    return os.path.join(output_dir, name)


@deprecated(
    version='0.0.2.dev1',
    reason="You should use the from com.dvsnier.directory.common_directory import CommonDirectory, that We will delete \
this method after extending 2-3 versions")
def generate_fmt_file_name(output_dir_name, file_name, fmt='%Y%m%d_%H%M%S'):
    'the generate out with fmt file name'
    output_dir = mk_output_dir(output_dir_name)
    name = str("%s_%s.txt" % (file_name, datetime.datetime.now().strftime(fmt)))
    return os.path.join(output_dir, name)


@deprecated(
    version='0.0.2.dev1',
    reason="You should use the from com.dvsnier.directory.common_directory import CommonDirectory, that We will delete \
this method after extending 2-3 versions")
def generate_file_name(output_dir_name, file_name):
    'the generate out file name'
    output_dir = mk_output_dir(output_dir_name)
    return os.path.join(output_dir, file_name)


@deprecated(
    version='0.0.2.dev1',
    reason="You should use the from com.dvsnier.directory.common_directory import CommonDirectory, that We will delete \
this method after extending 2-3 versions")
def generate_file_name_only(output_dir_name, file_name):
    'the generate file name only'
    output_dir = mk_dir(output_dir_name)
    return os.path.join(output_dir, file_name)


@deprecated(
    version='0.0.2.dev1',
    reason="You should use the from com.dvsnier.directory.common_directory import CommonDirectory, that We will delete \
this method after extending 2-3 versions")
def generate_complex_or_fmt_file_name(output_dir_name, file_name, fmt='%Y%m%d_%H%M%S'):
    'the generate out complex or fmt file name'
    output_dir = mk_output_dir(output_dir_name)
    if file_name is None or len(file_name.strip()) == 0:
        raise ValueError('the file name is invaild.')
    file_name = file_name.strip()
    if '.' in file_name:
        rdot_index = file_name.rfind('.')
        if rdot_index > 0:
            file_name = str("%s_%s%s" %
                            (file_name[0:rdot_index], datetime.datetime.now().strftime(fmt), file_name[rdot_index:]))
    else:
        file_name = str("%s_%s" % (file_name, datetime.datetime.now().strftime(fmt)))
    return os.path.join(output_dir, file_name)


@deprecated(
    version='0.0.2.dev1',
    reason="You should use the from com.dvsnier.directory.common_directory import CommonDirectory, that We will delete \
this method after extending 2-3 versions")
def mk_dir(output_dir_name):
    'the initialize global output dir'
    project_dir = os.path.abspath('.')
    output_dir = os.path.join(project_dir, output_dir_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir


@deprecated(
    version='0.0.2.dev1',
    reason="You should use the from com.dvsnier.directory.common_directory import CommonDirectory, that We will delete \
this method after extending 2-3 versions")
def mk_output_dir(output_dir_name):
    'the initialize output dir'
    # root_dir = os.path.dirname(os.path.abspath('.'))
    # logging.debug('the current root_dir is %s' % root_dir)
    project_dir = os.path.abspath('.')
    # logging.debug('the current project_dir is %s' % project_dir)
    # src_dir = os.path.join(project_dir, 'src')
    # logging.debug('the current src_dir is %s' % src_dir)
    out_dir = os.path.join(project_dir, 'out')
    # logging.debug('the current out_dir is %s' % out_dir)
    output_dir = os.path.join(out_dir, output_dir_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # logging.debug('the current output_dir is %s' % output_dir)
    return output_dir


@deprecated(
    version='0.0.2.dev1',
    reason="You should use the from com.dvsnier.directory.common_directory import CommonDirectory, that We will delete \
this method after extending 2-3 versions")
def mk_children_dir(output_dir_name, sub_dir_name):
    'the initialize children dir'
    if not os.path.exists(output_dir_name):
        os.makedirs(output_dir_name)
    children_dir = os.path.join(output_dir_name, sub_dir_name)
    if not os.path.exists(children_dir):
        os.makedirs(children_dir)
    # logging.debug('the current children_dir is %s' % children_dir)
    return children_dir
