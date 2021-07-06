# -*- coding:utf-8 -*-

import logging
import os
import re

from com.dvsnier.config.iconf import IConf


class Configuration(IConf, object):
    '''the Configuration class'''

    _config = {}

    def __init__(self):
        super(Configuration, self).__init__()

    def obtain_config(self, config_file):
        """the read xxx.cfg"""
        if not config_file or not os.path.exists(config_file):
            raise IOError('the current config path is not found.')
        logging.info('the start parsing the configuration file that is {}'.format(os.path.abspath(config_file)))
        with open(config_file) as file_handler:
            lines = file_handler.readlines()
        pattern_with_list = re.compile(r'(?<=\[).+?(?=\])')
        pattern_with_element = re.compile(r'((?<=\')[^,\b]+?(?=\'))|((?<=\")[^,\b]+?(?=\"))')
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
                        match_with_immature_list = pattern_with_list.search(suspicious_value)
                        if match_with_immature_list:  # list
                            immature_list_str_value = match_with_immature_list.group()
                            if immature_list_str_value:
                                # match_with_element = pattern_with_element.findall(element_value)
                                iterator_object_with_callback_type_is_match_object = pattern_with_element.finditer(
                                    immature_list_str_value)
                                if iterator_object_with_callback_type_is_match_object:
                                    the_default_element_list_with_parsed = list()
                                    for element_value in iterator_object_with_callback_type_is_match_object:
                                        the_default_element_list_with_parsed.append(element_value.group())
                                    self._config[key] = the_default_element_list_with_parsed
                                else:
                                    logging.warning(
                                        'the value({}) corresponding to the current key({}) is illegal, parsing failed, then its parsing has been ignored.'
                                        .format(suspicious_value, key))
                                    continue  # ignore invaild split value
                            else:
                                logging.warning(
                                    'the value({}) corresponding to the current key({}) is illegal, parsing failed, then its parsing has been ignored.'
                                    .format(suspicious_value, key))
                                continue  # ignore invaild split value
                        else:  # str
                            self._config[key] = suspicious_value
                    else:
                        self._config[key] = suspicious_value
        return self._config
