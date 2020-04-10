# -*- coding:utf8 -*
#lilred

import os


def search_file(path, str):

    for file in os.listdir(path):
        this_path = os.path.join(path, file)
        if os.path.isfile(this_path):
            if str in file:
                print('file exists' + this_path)
        else:
            search_file(this_path, str)

if __name__ == "__main__":
    search_file(os.path.abspath(""), "")


