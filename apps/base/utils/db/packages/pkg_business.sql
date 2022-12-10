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

    PROCEDURE SP_DF_ML IS 
        -- ALL DEPARTMENTS
        CURSOR C1 IS 
        SELECT id FROM VIVIENDA;
        -- DETAIL ROOM FOR DEPARTMENT
        CURSOR C2(pk VIVIENDA.ID%TYPE) IS
        SELECT
        ds.id as "id_sala",
        s.descripcion
        FROM DETALLE_SALA ds
        INNER JOIN SALA s
        ON s.id = ds.id_sal
        INNER JOIN INVENTARIO I
        ON i.id = ds.id_inv
        INNER JOIN VIVIENDA v
        ON v.id = i.id_viv
        WHERE i.id_viv = pk;
        
        -- DETAIL PRODUCTS FOR ROOMS
        CURSOR C3(pk DETALLE_SALA.ID%TYPE) IS
        SELECT p.descripcion
        FROM detalle_producto dp
        INNER JOIN PRODUCTO p
        ON dp.id_pro = p.id
        WHERE dp.id_det = pk;
            
        -- RECORD FOR CSV
        r_csv dataframe%rowtype;

    BEGIN

        PKG_UTILS.SP_TRUNCATE_TABLE('DATAFRAME');
        
        FOR x in C1
        LOOP
            r_csv.id := x.id;
            r_csv.rooms := NULL;
            r_csv.products := NULL;
            
            -- 2 CURSOR
            FOR y IN C2(x.id)
            LOOP
                BEGIN
                    -- rooms
                    r_csv.rooms := r_csv.rooms ||' '|| y.descripcion;
                    DBMS_OUTPUT.PUT_LINE(y.descripcion);
                    -- C3
                    FOR z IN C3(y."id_sala")
                    LOOP
                        BEGIN
                            r_csv.products := r_csv.products ||' '|| z.descripcion;
                            DBMS_OUTPUT.PUT_LINE(z.descripcion);
                        EXCEPTION
                            WHEN OTHERS THEN
                                DBMS_OUTPUT.PUT_LINE('No hay productos en esta sala');
                        END;
                    END LOOP;
                EXCEPTION
                    WHEN OTHERS THEN
                        DBMS_OUTPUT.PUT_LINE('No hay sala');
                END;
            END LOOP;
            
            PKG_UTILS.v_sql := 'INSERT INTO DATAFRAME (id,rooms,products) VALUES (:id, :rooms, :products)';
            EXECUTE IMMEDIATE PKG_UTILS.v_sql USING r_csv.id, nvl(LTRIM(r_csv.rooms),'N/A'), NVL(LTRIM(r_csv.products),'N/A');
            COMMIT;
            
        END LOOP;
        
    END SP_DF_ML;

    -- Procedimiento que actualiza las puntuación promedio de la propiedad
    PROCEDURE SP_UPDATE_SCORE IS 
        TYPE t_deptos IS TABLE OF vivienda%rowtype INDEX BY PLS_INTEGER;
        z PLS_INTEGER := 1;
        v_deptos t_deptos;
        v_avg_stars vivienda.estrellas%TYPE;
        v_id vivienda.id%type;
    BEGIN
        SELECT * BULK COLLECT INTO v_deptos FROM vivienda;
        FOR I IN v_deptos.FIRST()..v_deptos.LAST()
        LOOP
            BEGIN
                v_id := v_deptos(I).ID;
                v_avg_stars:= fn_avg_stars(v_id);
                -- Aquí debo actualizar las estrellas por el promedio de calificaciones
                pkg_utils.v_sql := 'UPDATE vivienda SET estrellas = :v_avg_stars 
                WHERE ID = :v_id AND estado = ''ACTIVO''';
                EXECUTE IMMEDIATE pkg_utils.v_sql
                USING v_avg_stars, v_id;
                IF sql%rowcount > 0 THEN
                    COMMIT;
                END IF;
            EXCEPTION
                WHEN OTHERS THEN
                    DBMS_OUTPUT.PUT_LINE('Error');
            END;
        END LOOP;
    END SP_UPDATE_SCORE;

END PKG_BUSINESS;
