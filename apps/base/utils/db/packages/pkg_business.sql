CREATE OR REPLACE PACKAGE BODY PKG_BUSINESS IS
     PROCEDURE SP_FINE_VALUE (p_pk check_out.id%type) IS
        CURSOR C1 IS 
        SELECT dp.id_est, dp.id_pro, p.precio,
        ds.id_inv, i.id_viv
        FROM DETALLE_PRODUCTO dp
        INNER JOIN PRODUCTO p
        ON p.id = dp.id_pro
        INNER JOIN DETALLE_SALA ds
        ON dp.id_det = ds.id
        INNER JOIN INVENTARIO I
        ON i.id = ds.id_inv
        INNER JOIN VIVIENDA v
        ON v.id = i.id_viv
        INNER JOIN RESERVA re
        ON re.id_viv = v.id
        INNER JOIN check_out ck
        ON re.id = ck.id_res
        WHERE ck.id = p_pk;
        
        v_ptc NUMBER(5,2);
        v_multa NUMBER(9) DEFAULT 0;
        v_monto NUMBER(9) DEFAULT 0;
     BEGIN
        FOR x in c1
        LOOP    
            BEGIN
                SELECT PORCENTAJE / 100 
                INTO v_ptc
                FROM TRAMO_MULTA
                WHERE id = x.id_est;
                
                
                IF x.id_est <> 1 THEN
                    v_monto := ROUND(x.precio * v_ptc);
                    v_multa := v_multa + v_monto;
                END IF;
                
                
            EXCEPTION
                WHEN OTHERS THEN
                    pkg_utils.v_error_code := SQLCODE;
                    pkg_utils.v_subprogram_name := 'PKG_UTILS.SP_FINE_VALUE';
                    pkg_utils.v_error_message := sqlerrm;
                    pkg_utils.sp_error_control(pkg_utils.v_error_code,pkg_utils.v_subprogram_name,pkg_utils.v_error_message);        
            END;
        END LOOP;
        
        -- Actualizar el valor de la multa
        UPDATE CHECK_OUT SET total_multa = v_multa WHERE id = p_pk;
        COMMIT;
        
     END SP_FINE_VALUE;
END PKG_BUSINESS;
