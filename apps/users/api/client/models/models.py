
# Modelos para hacer querys con procs

class Client(object):
    def __init__(self, resultado : str):
        self.resultado = resultado

    def to_json(self):
        return {
            'resultado': self.resultado
        }