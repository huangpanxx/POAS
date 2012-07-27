'''
Created on 2012-7-28

@author: snail
'''
class CSDBRouter(object):
    """A router to control all database operations on models in
    the myapp application"""

    def db_for_read(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        if model._meta.app_label == 'csadmin':
            return 'csadmin'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        if model._meta.app_label == 'csadmin':
            return 'csadmin'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in myapp is involved"
        if obj1._meta.app_label == 'csadmin' or obj2._meta.app_label == 'csadmin':
            return True
        return None

    def allow_syncdb(self, db, model): 
        "Make sure the myapp app only appears on the 'other' db" 
        if db == 'csadmin':
            return model._meta.app_label == 'csadmin'
        elif model._meta.app_label == 'csadmin':
            return False
        return None
