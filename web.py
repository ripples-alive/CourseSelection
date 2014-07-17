#!/usr/bin/python
#encoding:utf-8

import urllib
import urllib2
import cookielib


class Web:
    """Class to open URLs with cookies."""
    def __init__(self):
        try:
            cj = cookielib.CookieJar()
            self.__opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            self.__opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]

        except Exception, e:
            print(e)

    def open(self, url, data=None, method='POST'):
        """Return string for the specified URL."""
        try:
            if method == 'POST':
                if data is None:
                    return self.__opener.open(url).read()
                else:
                    return self.__opener.open(url, urllib.urlencode(data)).read()
            elif method == 'GET':
                return self.__opener.open(url + '?' + urllib.urlencode(data)).read()
        except Exception, e:
            print(e)
