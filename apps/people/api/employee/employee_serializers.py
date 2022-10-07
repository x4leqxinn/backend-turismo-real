from rest_framework import serializers
from apps.base.models.db_models import Empleado
from apps.locations.models import Cities

class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        fields = '__all__'

    def to_representation(self,instance):
        # Buscamos la ciudad a la que pertenece
        city = Cities.objects.get(id = instance.id.id_ciu)
        return{
            'id' : instance.id.id,
            'run' : instance.id.run,
            'dv' : instance.id.dv,
            'pasaporte' : instance.id.pasaporte,
            'nombre' :instance.id.nombre,
            'snombre' :instance.id.snombre,
            'ap_paterno' :instance.id.ap_paterno,
            'ap_materno' :instance.id.ap_materno,
            'fecha_nacimiento' : instance.id.fecha_nacimiento,
            'telefono' :instance.id.telefono,
            'num_calle' :instance.id.num_calle,
            'calle' :instance.id.calle,
            'doc_identidad' : {
                'id' : instance.id.id_doc.id,
                'descripcion' : instance.id.id_doc.descripcion
            },
            'estado_civil' : {
                'id' : instance.id.id_est1.id,
                'descripcion' : instance.id.id_est1.descripcion
            },
            'genero' : {
                'id' : instance.id.id_gen.id,
                'descripcion' : instance.id.id_gen.descripcion
            },
            'sueldo':instance.sueldo,
            'fecha_contrato' :instance.fecha_contrato,
            'id_car' :{
                'id':instance.id_car.id,
                'descripcion':instance.id_car.descripcion
            },
            'pais' : {
                'id' : city.country.id,
                'nombre' : city.country.name,
            },
            'estado_pais' : {
                'id' : city.state.id,
                'nombre' : city.state.name,
            },
            'ciudad' : {
                'id' : city.id,
                'nombre' : city.name
            }
        }

