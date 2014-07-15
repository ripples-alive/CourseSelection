#!/usr/bin/python
#encoding:utf-8

import getpass

from course import CourseConnect

username = '12307130267'
password = getpass.getpass('请输入选课密码：')

connect = CourseConnect(username, password)

courseID = raw_input('请输入选课号：')

while True:
    result = connect.selectCourse(courseID)
    print result
