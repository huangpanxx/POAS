#coding:utf8
'''
Created on 2012-7-13

@author: snail
'''
#解码数据
import chardet
def decodeHtml(data):
    char = chardet.detect(data)
    char = char['encoding']
    if char:
        data = unicode(data, char, 'ignore').encode('utf-8')
    return data
