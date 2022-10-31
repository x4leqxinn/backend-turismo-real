CREATE OR REPLACE TRIGGER TRG_MOV_VAL
BEFORE INSERT ON MOVILIZACION
FOR EACH ROW
DECLARE
    v_capacidad VEHICULO.capacidad%Type;
BEGIN 
    IF :new.asientos_disp IS NULL THEN

        -- Asignamos al servicio los asientos disponibles 
        SELECT capacidad INTO v_capacidad
        FROM VEHICULO 
        WHERE id = :new.id_veh;

        :new.asientos_disp := v_capacidad - 1;

    END IF;
END TRG_MOV_VAL;
