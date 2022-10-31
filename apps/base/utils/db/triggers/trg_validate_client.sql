CREATE OR REPLACE TRIGGER TRG_DET_SERV_MOV
AFTER INSERT ON DETALLE_SERVICIO
FOR EACH ROW
DECLARE
    v_total RESERVA.cant_total%Type;
BEGIN
    -- Restar la cant de asientos disponibles
    SELECT cant_total into v_total
    FROM RESERVA
    WHERE id = :new.id_res;

    UPDATE movilizacion SET asientos_disp = asientos_disp - v_total WHERE id = :new.ID_SER;
END TRG_DET_SERV_MOV;