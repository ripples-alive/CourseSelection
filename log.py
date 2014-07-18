#!/usr/bin/env python
# encoding:utf-8

import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def write_log(content):
    """Write content into log file."""
    log = open('.log', 'a')
    log.write(time.strftime('%Y-%m-%d %H:%M:%S'))
    log.write(' : ')

    # if type(content) == type(''):
    if isinstance(content, str):
        log.write(content + '\n')
    elif content is not None:
        for row in content:
            for item in row:
                log.write(item)
                log.write('\t')
            log.write('\n')

    log.write('\n')
    log.close()
