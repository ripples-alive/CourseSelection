#!/usr/bin/python
#encoding:utf-8

import os


def get_code(content):
    img_file = open(r'identify\IdCode.jpg', 'wb')
    img_file.write(content)
    img_file.close()
    
    os.system(r'identify\run.bat')
    
    code_file = open(r'identify\output.txt', 'r')
    ans = ''
    for i in xrange(4):
        ans += chr(int(code_file.readline()))

    return ans
