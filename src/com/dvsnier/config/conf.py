# -*- coding:utf-8 -*-

import configparser

from com.dvsnier.config.iconf import IConf


class Conf(IConf, object):
    'the config or property class'

    def __init__(self):
        super(Conf, self).__init__()
        # protected property
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
                      (section_element, option_element, self._config.get(section_element, option_element)))
