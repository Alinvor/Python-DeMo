# -*- coding:utf-8 -*-

import configparser
import logging
from com.dvsnier.directory.common_dir import generate_complex_file_name


def logging_conf(kwargs):
    '''
    the logging conf info:
    logging_conf(**kwargs={output_dir_name=\' \', file_name=\' \'})
    '''
    if kwargs.get('output_dir_name') is None or len(
            kwargs.get('output_dir_name')) == 0:
        raise KeyError('the current kwargs[output_dir_name] is empty.')
    if kwargs.get('file_name') is None or len(kwargs.get('file_name')) == 0:
        raise KeyError('the current kwargs[file_name] is empty.')
    file_name = generate_complex_file_name(kwargs['output_dir_name'],
                                           kwargs['file_name'])
    logging.basicConfig(
        filename=file_name,
        filemode='a',
        format='[%(asctime)s][%(levelname)8s] --- %(message)s',
        # format=
        # '[%(asctime)s][%(levelname)8s][%(filename)s:%(lineno)s] --- %(message)s',
        level=logging.DEBUG)
    logging.info('this current file is %s' % (file_name))


class Conf(object):
    'the config or property class'
    _config = None

    def __init__(self):
        super(Conf, self).__init__()
        self._config = configparser.ConfigParser()

    def write(self, file):
        'the write config to file'
        if file is None or file == '' or len(file) == 0:
            raise KeyError('the file is invalid.')
        # no allow 'a' sign mask, otherwise raise DuplicateSectionError
        with open(file, 'w') as f:
            self._config.write(f)

    def read(self, file):
        'the read config file'
        if file is None or file == '' or len(file) == 0:
            raise KeyError('the file is invalid.')
        self._config.read(file)

    def add_section(self, section):
        'the add section'
        if section is None or section == '' or len(section) == 0:
            raise KeyError('the section is invalid.')
        if section not in self.sections():
            self._config.add_section(section)

    def remove_section(self, section):
        'the remove section'
        if section is None or section == '' or len(section) == 0:
            raise KeyError('the section is invalid.')
        if section in self.sections():
            self._config.remove_section(section)

    def sections(self):
        'the return section list'
        return self._config.sections()

    def options(self, section):
        'the get section item'
        if section is None or section == '' or len(section) == 0:
            raise KeyError('the section is invalid.')
        return self._config.options(section)

    def get(self, section, option):
        'the get option value with section'
        if section is None or section == '' or len(section) == 0:
            raise KeyError('the section is invalid.')
        if option is None or option == '' or len(option) == 0:
            raise KeyError('the option is invalid.')
        return self._config.get(section, option)

    def getboolean(self, section, option):
        'the get option value with section'
        if section is None or section == '' or len(section) == 0:
            raise KeyError('the section is invalid.')
        if option is None or option == '' or len(option) == 0:
            raise KeyError('the option is invalid.')
        return self._config.getboolean(section, option)

    def getfloat(self, section, option):
        'the get option value with section'
        if section is None or section == '' or len(section) == 0:
            raise KeyError('the section is invalid.')
        if option is None or option == '' or len(option) == 0:
            raise KeyError('the option is invalid.')
        return self._config.getfloat(section, option)

    def getint(self, section, option):
        'the get option value with section'
        if section is None or section == '' or len(section) == 0:
            raise KeyError('the section is invalid.')
        if option is None or option == '' or len(option) == 0:
            raise KeyError('the option is invalid.')
        return self._config.getint(section, option)

    def set(self, section, option, value):
        'the set section option value with dict style'
        self.add_section(section)
        if option is None or option == '' or len(option) == 0:
            raise KeyError('the option is invalid.')
        # if value is None or value == '' or len(value) == 0:
        #     raise KeyError('the value is invalid.')
        self._config.set(section, option, value)

    def debug(self):
        'the debug config information'
        for section_element in self._config.sections():
            options = self._config.options(section_element)
            for option_element in options:
                print('option: %s, key: %s, value: %s' %
                      (section_element, option_element,
                       self._config.get(section_element, option_element)))
