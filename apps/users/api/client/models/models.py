
# Modelos para hacer querys con procs

class Client(object):
    def __init__(self, rut : str, dv : str, pasaporte : str, 
                nombre : str, snombre :str, ap_paterno : str,
                ap_materno : str, fecha_nacimiento : str, telefono : str,
                num_calle : str, calle : str, id_ciu : int, id_est : int,
                id_pai : int, id_doc : int, id_est_civ : int, id_gen : int ):
        
        self.rut = rut
        self.dv = dv
        self.pasaporte = pasaporte
        self.nombre = nombre
        self.snombre = snombre
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.num_calle = num_calle
        self.calle = calle
        self.id_ciu = id_ciu
        self.id_est = id_est
        self.id_pai = id_pai
        self.id_doc = id_doc
        self.id_est_civ = id_est_civ
        self.id_gen = id_gen

    def to_json(self):
        return {
            'nombre': self.nombre
        }