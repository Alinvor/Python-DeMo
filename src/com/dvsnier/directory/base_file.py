# -*- coding:utf-8 -*-

import datetime
import os
import time

from com.dvsnier.directory.abstract_directory import AbstractDirectory


class BaseFile(AbstractDirectory, object):
    '''the Common Directory class that strict patterns are strongly recommended to constrain the determination of input path rules'''
    def __init__(self, strategy_mode=False):
        super(BaseFile, self).__init__(strategy_mode)

    def generate_complex_file_name(self, output_dir_name, file_name):
        'the generate complex file name'
        output_dir = self.mk_output_dir(output_dir_name)
        name = str("%s_%s.log" % (file_name, int(time.time())))
        return os.path.join(output_dir, name)

    def generate_fmt_file_name(self, output_dir_name, file_name, fmt='%Y%m%d_%H%M%S'):
        'the generate out with fmt file name'
        output_dir = self.mk_output_dir(output_dir_name)
        name = str("%s_%s.txt" % (file_name, datetime.datetime.now().strftime(fmt)))
        return os.path.join(output_dir, name)

    def generate_file_name(self, output_dir_name, file_name):
        'the generate out file name'
        output_dir = self.mk_output_dir(output_dir_name)
        return os.path.join(output_dir, file_name)

    def generate_file_name_only(self, output_dir_name, file_name):
        'the generate file name only'
        output_dir = self.mk_dir(output_dir_name)
        return os.path.join(output_dir, file_name)

    def generate_complex_or_fmt_file_name(self, output_dir_name, file_name, fmt='%Y%m%d_%H%M%S'):
        'the generate out complex or fmt file name'
        output_dir = self.mk_output_dir(output_dir_name)
        if file_name is None or len(file_name.strip()) == 0:
            raise ValueError('the file name is invaild.')
        file_name = file_name.strip()
        if '.' in file_name:
            rdot_index = file_name.rfind('.')
            if rdot_index > 0:
                file_name = str(
                    "%s_%s%s" %
                    (file_name[0:rdot_index], datetime.datetime.now().strftime(fmt), file_name[rdot_index:]))
        else:
            file_name = str("%s_%s" % (file_name, datetime.datetime.now().strftime(fmt)))
        return os.path.join(output_dir, file_name)
