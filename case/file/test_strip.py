# -*- coding:utf-8 -*-

import os


def read_file(file_name):
    'the read file with reg'
    if file_name is not None:
        index = 0
        content = []
        for line in open(file_name, 'r'):
            if len(line.strip()) > 0:
                index += 1
                md_line_text = line.strip().split('[')
                line_text = str(
                    str(index) + '. [' + md_line_text[1] +
                    md_line_text[0]).encode('utf-8')
                content.append(line_text)
                # print(line_text)
        dir_name = os.path.dirname(file_name)
        dest_name = os.path.join(dir_name, 'out_asc.txt')
        if len(content) > 0:
            with open(dest_name, 'w') as file:
                for item in content:
                    file.write(str(item).encode('utf-8') + '\n')


if __name__ == "__main__":
    '''正则拆分按行读文件，写入MD 文件'''
    # 指定位置文件 ./out/asc.txt
    out_dir = os.path.join(os.getcwd(), 'out')
    file = os.path.join(out_dir, 'asc.txt')
    if os.path.isfile(file):
        read_file(file)
