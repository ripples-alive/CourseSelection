#!/usr/bin/python
#encoding:utf-8

import urllib2
import re

from web import Web

class CourseConnect:
    def __init__(self, username, password):
        self.__connect = Web()
        self.__baseUrl = 'http://xk.fudan.edu.cn/xk/'

        self.__login(username, password)

    def __login(self, username, password):
        self.__username = username
        self.__password = password

        content = self.__connect.open(self.__baseUrl + 'image.do')

        imgFile = open('identify.jpg', 'w')
        imgFile.write(content)
        imgFile.close()

        data = {'studentId' : self.__username, 'password' : self.__password, \
            'rand' : raw_input('请输入验证码：'), 'Submit2' : '提交'}

        self.__connect.open(self.__baseUrl + 'loginServlet', data)

    def selectCourse(self, courseID):
        content = self.__connect.open(self.__baseUrl + 'input.jsp')

        pattern = re.compile(ur'<input[^>]*name="token"[^>]*value="([^>]*)"[^>]*/>')
        results = pattern.findall(content)
        token = results[0]

        data = {'token' : token}
        content = self.__connect.open(self.__baseUrl + 'image.do', data, 'GET')

        imgFile = open('identify.jpg', 'w')
        imgFile.write(content)
        imgFile.close()

        data = {'token' : token, 'selectionId' : courseID, \
            'xklb' : 'ss', 'rand' : raw_input('请输入验证码：')}

        content = self.__connect.open(self.__baseUrl + 'doSelectServlet', data)
        pattern = re.compile(ur'function start_alert[^"]*"([^"]*)"')
        results = pattern.findall(content)
        return results[0]
