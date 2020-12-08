# -*- coding:utf-8 -*-

import collections
import json
# import pprint

tags = {
    'a': 2,
    'v0.0.2': {
        'stamp': 1576053555,
        'date': '2019-12-11',
        'authors': {
            'DovSnier': 3
        },
        'hash': 'b76da094137669d3eb3edc985391366bc2bb93b9',
        'commits': 22
    },
    'bc': '32',
    'ac': {},
    'v0.0.3': {
        'stamp': 1576053555,
        'date': '2019-12-21',
        'authors': {
            'DovSnier': 3
        },
        'hash': 'b76da094137669d3eb3edc985391366bc2bb93b9',
        'commits': 23
    },
    'v0.0.1': {
        'stamp': 1576053555,
        'date': '2019-12-1',
        'authors': {
            'DovSnier': 3
        },
        'hash': 'b76da094137669d3eb3edc985391366bc2bb93b9',
        'commits': 21
    },
    's': ['2020-01-09', '2020-01-10']
}


def test_dict_sort_slowly():
    ''' 使用sorted 会生成新的list，导致性能下降，建议使用内置sort '''
    global tags
    tags_tuple_list = sorted(tags.items())
    # tags_tuple_list = sorted(tags.items(), key=lambda element: element[1])
    print('\n')
    print(tags_tuple_list)
    tags.clear()
    print("tags is %s" % tags)
    for item in tags_tuple_list:
        tags[item[0]] = item[1]
    print("tags is %s" % tags)


def test_dict_sort():
    global tags
    # print(tags.items())
    keys = tags.keys()
    keys.sort()
    # tuple_with_tags = [(key, tags[key]) for key in keys]
    # print("%s\n%s" % (type(tuple_with_tags), tuple_with_tags))
    tags_with_sort = collections.OrderedDict()  # 有序字典
    for key in keys:
        # tags_with_sort.setdefault(key, tags[key])
        tags_with_sort[key] = tags[key]
    tags = tags_with_sort

    # prettyPrinter = pprint.PrettyPrinter(indent=4)
    # prettyPrinter.pprint(tags)

    json_list = json.dumps(tags, indent=4)
    print(json_list)

    # print()
    # print(tags)


def test_print():
    '''
        {
            'v0.0.1':
            {
                'stamp': 1576053555,
                'date': '2019-12-1',
                'commits': 21,
                'hash': 'b76da094137669d3eb3edc985391366bc2bb93b9',
                'authors':
                {
                    'DovSnier': 3
                }
            },
            'v0.0.2':
            {
                'stamp': 1576053555,
                'date': '2019-12-11',
                'commits': 22,
                'hash': 'b76da094137669d3eb3edc985391366bc2bb93b9',
                'authors':
                {
                    'DovSnier': 3
                }
            },
            'v0.0.3':
            {
                'stamp': 1576053555,
                'date': '2019-12-21',
                'commits': 23,
                'hash': 'b76da094137669d3eb3edc985391366bc2bb93b9',
                'authors':
                {
                    'DovSnier': 3
                }
            }
        }
    '''
    pass


if __name__ == "__main__":
    '''主函数入口'''
    test_dict_sort()
    # test_dict_sort_slowly()
