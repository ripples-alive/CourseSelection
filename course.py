#!/usr/bin/env python
#encoding:utf-8

import re

from web import Web


def get_code(picture):
    """Get the code in the picture."""
    img_file = open('identify.jpg', 'w')
    img_file.write(picture)
    img_file.close()
    return raw_input('请输入验证码：')


class CourseConnect:
    def __init__(self, username, password):
        """Initialize with specific username and password."""
        self.__connect = Web()
        self.__baseUrl = 'http://xk.fudan.edu.cn/xk/'

        self.__login(username, password)

    def __login(self, username, password):
        # Login course selection system with specific username and password.
        self.__username = username
        self.__password = password

        # Get identify code for login.
        content = self.__connect.open(self.__baseUrl + 'image.do')
        identify_code = get_code(content)

        data = {'studentId': self.__username, 'password': self.__password,
                'rand': identify_code, 'Submit2': '提交'}
        self.__connect.open(self.__baseUrl + 'loginServlet', data)

    def select_course(self, course_id):
        """Select specific course once."""
        # Get token for selecting course.
        content = self.__connect.open(self.__baseUrl + 'input.jsp')
        pattern = re.compile(ur'<input[^>]*name="token"[^>]*value="([^>]*)"[^>]*/>')
        results = pattern.findall(content)
        token = results[0]

        # Get identify code for selecting course.
        data = {'token': token}
        content = self.__connect.open(self.__baseUrl + 'image.do', data, 'GET')
        identify_code = get_code(content)

        # Select course and get the result of selection.
        data = {'token': token, 'selectionId': course_id,
                'xklb': 'ss', 'rand': identify_code}
        content = self.__connect.open(self.__baseUrl + 'doSelectServlet', data)
        pattern = re.compile(ur'function start_alert[^"]*"([^"]*)"')
        results = pattern.findall(content)
        return results[0]
