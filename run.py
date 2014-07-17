#!/usr/bin/python
#encoding:utf-8

import getpass

from course import CourseConnect
from log import write_log

username = '12307130267'
password = getpass.getpass('请输入选课密码：')
connect = CourseConnect(username, password)

courseID = raw_input('请输入选课号：')

while True:
    result = connect.select_course(courseID)
    print(result)
    write_log(result)
