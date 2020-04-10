# -*- coding:utf8 -*
#lilred

import os

def search_file(path, str):
    try:
        assert str in os.listdir(path)
        return "exists"
    except Exception as e:
        print(e)

