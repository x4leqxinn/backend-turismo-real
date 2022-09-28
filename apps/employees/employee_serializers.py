from rest_framework import serializers

from apps.base.models.db_models import Empleado


class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        fields = '__all__'

    def to_representation(self,instance):
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
            'pais' : {
                'id' : instance.id.id_pai.id,
                'nombre' : instance.id.id_pai.nombre,
            },
            'id_est' : {
                'id' : instance.id.id_est.id,
                'nombre' : instance.id.id_est.nombre,
            },
            'id_ciu' : {
                'id' : instance.id.id_ciu.id,
                'nombre' : instance.id.id_ciu.nombre
            },
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
            }
        }

    