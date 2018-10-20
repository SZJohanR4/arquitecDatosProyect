from usuario import middleware

class RouterBaseDatos(object):

    def db_lector(self, model, **hints):
        return middleware.prueba

    def db_escritor(self, model, **hints):
        return middleware.prueba
