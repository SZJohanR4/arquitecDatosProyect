from django.conf import settings
from datetime import datetime
import socket, os

class replicacion:
    def __init__(self, get_response):
        if self.conexion_a_db('default'):
            db = 'MAESTRO'
        elif  self.conexion_a_db('esclavo'):
            db = 'ESCLAVO A'
        print("==============Conectado al servidor: "+db+" ==============")
        return None

    def prueba():
        if self.conexion_a_db("default"):
            db = 'MAESTRO'
        elif  self.conexion_a_db('esclavo'):
            db = 'ESCLAVO A'
        print("==============Conectado al servidor: "+db+" ==============")
        return db

    def conexion_a_db(self,database_name):
        try:
            db_definition = getattr(settings, 'DATABASES')[database_name]
            s = socket.create_connection((db_definition['HOST'], db_definition['PORT']), 5)
            s.close()
            return True
        except Exception as e:
            return False
