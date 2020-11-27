# -*- coding:utf-8 -*-


def test_map():
    tags = {
        'v0.0.2': {
            'stamp': 1576053555,
            'date': '2019-12-11',
            'authors': {
                'DovSnier': 3
            },
            'hash': 'b76da094137669d3eb3edc985391366bc2bb93b9',
            'commits': 22
        },
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
        }
    }
    # lambda
    list_o = map(lambda el: (el[1]['date'], el[0]), tags.items())

    # function
    # list_o = map(test_tuple, tags.items())

    print list_o
    tags_sorted_by_date_desc = map(lambda el: el[1], reversed(sorted(list_o)))
    print tags_sorted_by_date_desc


def test_tuple(element):
    return (element[1]['date'], element[0])


if __name__ == "__main__":
    '''主函数入口'''
    test_map()
