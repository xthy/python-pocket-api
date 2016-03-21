#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pocket
api = pocket.Api(consumer_key='<input>', access_token='<input>')
items_list = api.get(contentType='video')

try:
    f=open('videos.txt','w')
    for item in items_list:
            if type(item.title) == unicode:
                f.write(item.id)
                f.write('\t')
                f.write(unicode.encode(item.title))
                f.write('\t')
                f.write(item.given_url)
                f.write('\n')
            elif type(item.title) ==str:
                f.write(item.id)
                f.write('\t')
                f.write(item.title)
                f.write('\t')
                f.write(str(item.given_url))
                f.write('\n')
            else:
                f.write(item.id)
                f.write('\t')
                f.write('\t')
                f.write(item.given_url)
                f.write('\n')
except Exception, e:
	print e
	sys.exit(2)

f.close()