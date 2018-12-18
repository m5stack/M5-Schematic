#-*-coding:utf-8-*-

import os
import sys
import re

def rename_file(filename):
    new_name = re.split('[_]')


files_list = os.listdir(".")
for i in files_list:
    i = i.lower()
    print(i)
