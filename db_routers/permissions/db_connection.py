# Aquí le otorgamos el usuario 
# con el cuál debe conectarse al esquema
def oracle_connection(permission):      
    if permission == 1:
        return 'turismo_real'
    return None
