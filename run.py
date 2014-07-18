#!D:\Python27\python.exe
#encoding:utf-8

import getpass
import time

from course import CourseConnect
from log import write_log

username = '12307130267'
password = getpass.getpass('Please input URP password:')
connect = CourseConnect(username, password)

course_id = raw_input('Please input the course ID:')

delay_time = int(raw_input('Please input the delay time between select course:'))

while True:
    result = connect.select_course(course_id)
    print(result)
    write_log(result)
    time.sleep(delay_time)
