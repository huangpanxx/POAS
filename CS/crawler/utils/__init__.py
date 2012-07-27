#coding:utf8

def getClassFullName(obj):
    t = type(obj)
    return '%s.%s' % (t.__module__,t.__name__) 

def create_class(class_name, bases=(object,), attributes={}):
    cls = type.__new__(type, class_name, bases, attributes)
    super(type, cls).__init__(class_name, bases, attributes)
    return cls
