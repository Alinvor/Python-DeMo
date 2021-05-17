# -*- coding:utf-8 -*-

import configparser

file_name = 'conf/configParse.conf'


def writeConfig():
    'the write config'
    config = configparser.ConfigParser()
    config["DEFAULT"] = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}
    config['SELECTION_ONE'] = {'A': 1, 'one': '1'}
    config['SELECTION_TWO'] = {'B': 2, 'two': 2}
    with open(file_name, 'w') as file:
        config.write(file)


def readConfig():
    'the read config'
    config = configparser.ConfigParser()
    config.read(file_name)
    print(config.sections())
    # print(config.options('SELECTION_ONE'))
    # print(config.options('SELECTION_TWO'))
    #
    # print(config.items('SELECTION_ONE'))
    # print (config.items('SELECTION_TWO'))
    #
    # print(config.get('SELECTION_ONE', 'ONE'))
    # print(config.getint('SELECTION_ONE', 'ONE'))
    # print(config.get('SELECTION_TWO', 'TWO'))


def repairedConfig():
    'the repaired config'
    config = configparser.ConfigParser()
    config.read(file_name)
    print(config.sections())
    config.add_section('add_section')
    config.remove_section('add_section')

    if 'set_section' not in config:
        config.add_section('set_section')

    config.set('set_section', 'set_option', 'set_value')
    config.set('set_section', 'DovSnieir', '资深好男人')
    print(config.sections())
    with open(file_name, 'w') as file:
        config.write(file)


if __name__ == "__main__":
    '''主函数入口'''
    # 写
    writeConfig()
    # 修
    repairedConfig()
    # 读
    readConfig()
