#coding:utf8

def getClassFullName(obj):
    t = type(obj)
    return '%s.%s' % (t.__module__,t.__name__) 