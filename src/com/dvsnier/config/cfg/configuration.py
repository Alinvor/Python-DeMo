# -*- coding:utf-8 -*-

import logging
from numbers import Number
import os
import re

from com.dvsnier.config.iconf import IConf


class Configuration(IConf, object):
    '''
        the Configuration class that provides the ability to parse configuration files

        ## Illustration or Description

        The types of data structures supported are as follows:

        - str
        - number
        - boolean
        - list

        The standard writing method of each data type is given below:

        ### str types

            At present, the system supports three formats by default:
            - `key = value` # The first is recommendation pattern
            - `key = 'value'`
            - `key = "value"`

        ### number types

            - `key = number`

        ### boolean types

            - `key = true` # The first is recommendation pattern
            - `key = True`
            - `key = false` # The first is recommendation pattern
            - `key = False`

        ### list types

            At present, it only supports the case that the content array is of the same type constraint, and the default is `str` generic:

            - `key = ['value0', 'value1', ...]`
            - `key = ['value0', "value1", ...]`
            - `key = ["value0", "value1", ...]` # The first is recommendation pattern

        ## Warning
            - All support granularity, only support when `single line mode`, do not support multi line mode.
            - Illegal data will be ignored.
    '''

    __pattern_with_list = re.compile(r'(?<=\[).+?(?=\])')
    __pattern_with_number_element = re.compile(r'\b\d+?\b')
    __pattern_with_boolean_element = re.compile(r'\btrue|True|false|False\b')
    __pattern_with_element = re.compile(r'((?<=\')[^,\b]+?(?=\'))|((?<=\")[^,\b]+?(?=\"))')
    __pattern_with_element_strip = re.compile(r'(?<=\').+?(?=\')|(?<=\").+?(?=\")')

    def __init__(self):
        super(Configuration, self).__init__()
        # private property
        self.__config = {}

    def obtain_config(self, config_file):
        """the read xxx.cfg"""
        if not config_file or not os.path.exists(config_file):
            raise IOError('the current config path is not found.')
        logging.info('the start parsing the configuration file that is {}'.format(os.path.abspath(config_file)))
        with open(config_file) as file_handler:
            lines = file_handler.readlines()
        for line in lines:
            if line.strip().startswith('#'):
                continue  # ignore notes
            else:
                try:
                    split_at = line.index("=")
                except ValueError:
                    continue  # ignore bad/empty lines
                else:
                    # self._config[line[:split_at].strip()] = line[split_at + 1:].strip()
                    key = line[:split_at].strip()
                    suspicious_value = line[split_at + 1:].strip()
                    # https://docs.python.org/zh-cn/2.7/library/re.html?
                    # logging.debug('the key is {} and value is {}'.format(key, suspicious_value))
                    if suspicious_value:
                        match_with_immature_list = self.__pattern_with_list.search(suspicious_value)
                        match_with_immature_digital = self.__pattern_with_number_element.search(suspicious_value)
                        match_with_immature_boolean = self.__pattern_with_boolean_element.search(suspicious_value)
                        if match_with_immature_list:  # list
                            self.__resolve_with_list(match_with_immature_list, key, suspicious_value)
                        elif match_with_immature_digital:  # digital
                            self.__resolve_with_digital(match_with_immature_digital, key, suspicious_value)
                        elif match_with_immature_boolean:  # boolean
                            self.__resolve_with_boolean(match_with_immature_boolean, key, suspicious_value)
                        else:  # str
                            self.__resolve_with_str(key, suspicious_value)
                    else:
                        self.__resolve_with_str(key, suspicious_value)
        return self.__config

    def __resolve_with_list(self, match_with_immature_list, key, suspicious_value):
        'the resolve list data structure'
        immature_list_str_value = match_with_immature_list.group()
        if immature_list_str_value:
            iterator_object_with_callback_type_is_match_object = self.__pattern_with_element.finditer(
                immature_list_str_value)
            if iterator_object_with_callback_type_is_match_object:
                the_default_element_list_with_parsed = list()
                for element_value in iterator_object_with_callback_type_is_match_object:
                    the_default_element_list_with_parsed.append(element_value.group())
                self.__config[key] = the_default_element_list_with_parsed
            else:
                # ignore invaild split value
                logging.warning(
                    'the value({}) corresponding to the current key({}) is illegal, parsing failed, then its parsing has been ignored.'
                    .format(suspicious_value, key))
        else:
            # ignore invaild split value
            logging.warning(
                'the value({}) corresponding to the current key({}) is illegal, parsing failed, then its parsing has been ignored.'
                .format(suspicious_value, key))

    def __resolve_with_digital(self, match_with_immature_digital, key, suspicious_value):
        'the resolve digital data structure'
        element_value = match_with_immature_digital.group()
        try:
            if element_value and suspicious_value == element_value and isinstance(int(element_value), Number):
                self.__config[key] = int(element_value)
            else:
                self.__resolve_with_str(key, suspicious_value)
        except ValueError:
            self.__resolve_with_str(key, suspicious_value)

    def __resolve_with_boolean(self, match_with_immature_boolean, key, suspicious_value):
        'the resolve boolean data structure'
        element_value = match_with_immature_boolean.group()
        try:
            if element_value and suspicious_value == element_value:
                if 'true' == element_value or 'True' == element_value:
                    self.__config[key] = bool(1)
                else:
                    self.__config[key] = bool(0)
            else:
                self.__resolve_with_str(key, suspicious_value)
        except ValueError:
            self.__resolve_with_str(key, suspicious_value)

    def __resolve_with_str(self, key, suspicious_value):
        'the resolve str data structure'
        match_with_immature_str = self.__pattern_with_element_strip.search(suspicious_value)
        if match_with_immature_str:
            self.__config[key] = match_with_immature_str.group()
        else:
            self.__config[key] = suspicious_value
