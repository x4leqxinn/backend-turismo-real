class TurismoRealRouter:

    def db_for_read(self, model, **hints):
        return 'turismo_real'

    def db_for_write(self, model, **hints):
        return 'turismo_real'
    
    def allow_relation(self, obj1, obj2, **hints):
        return True
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'turismo_real'

