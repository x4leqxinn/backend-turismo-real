CREATE OR REPLACE PACKAGE BODY PKG_UTILS IS
    -- CONTROL DE ERRORES
    PROCEDURE SP_ERROR_CONTROL(p_cod_error ERROR_PROCESO.COD_ERROR%TYPE, p_subprogram ERROR_PROCESO.SUBPROGRAMA%TYPE, p_message ERROR_PROCESO.MENSAJE_ERROR%TYPE) IS
    BEGIN
        V_SQL := 'INSERT INTO ERROR_PROCESO (ID,COD_ERROR,SUBPROGRAMA,MENSAJE_ERROR,CREACION) VALUES (SEQ_ERROR_PROCESO.NEXTVAL,:p_cod_error,:p_subprogram,:p_message,SYSTIMESTAMP)';
        EXECUTE IMMEDIATE v_sql
        USING p_cod_error, p_subprogram, p_message;
        COMMIT;
    END SP_ERROR_CONTROL;
    
    FUNCTION FN_GET_AGE(p_birthday DATE) RETURN NUMBER IS
        v_age NUMBER(3) DEFAULT 0;
    BEGIN
        v_age := TRUNC(MONTHS_BETWEEN(SYSDATE,TO_DATE(p_birthday))/12);
        RETURN v_age;
    EXCEPTION
        WHEN OTHERS THEN
            v_error_code:= SQLCODE;
            v_subprogram_name := 'PKG_UTILS.FN_GET_AGE';
            v_error_message := SQLERRM;
            SP_ERROR_CONTROL(v_error_code,v_subprogram_name,v_error_message);
            RETURN v_age;
    END FN_GET_AGE;
    
    PROCEDURE SP_DELETE_ENTITY(p_id IN NUMBER, p_table IN VARCHAR2, p_out OUT NUMBER) IS 
    BEGIN
        p_out := 0;
        v_sql := 'UPDATE ' || p_table  || ' SET ESTADO = ''INACTIVO'', ACTUALIZACION = SYSTIMESTAMP WHERE id = :p_id';
        EXECUTE IMMEDIATE v_sql USING p_id;
        IF sql%rowcount > 0 THEN
            p_out := 1;
            COMMIT;
        END IF;
    EXCEPTION 
        WHEN OTHERS THEN
            v_error_code := SQLCODE;
            v_subprogram_name := 'PKG_UTILS.SP_DELETE_ENTITY';
            v_error_message := sqlerrm;
            sp_error_control(v_error_code,v_subprogram_name,v_error_message);
    END SP_DELETE_ENTITY;
    
    PROCEDURE SP_CHANGE_STATE_ENTITY(p_id IN NUMBER, p_table IN VARCHAR2, p_state IN VARCHAR2, p_out OUT NUMBER) IS
    BEGIN
        p_out := 0;
        v_sql := 'UPDATE ' || p_table || ' SET ESTADO = :p_state, ACTUALIZACION = SYSTIMESTAMP WHERE id = :p_id';
        EXECUTE IMMEDIATE v_sql USING p_state, p_id;
        IF sql%rowcount > 0 THEN
            p_out := 1;
            COMMIT;
        END IF;        
    EXCEPTION
        WHEN OTHERS THEN
            v_error_code := SQLCODE;
            v_subprogram_name := 'PKG_UTILS.SP_CHANGE_STATE_ENTITY';
            v_error_message := sqlerrm;
            sp_error_control(v_error_code,v_subprogram_name,v_error_message);
    END SP_CHANGE_STATE_ENTITY;
    
    PROCEDURE SP_UPDATE_FIELD(p_id IN NUMBER, p_table IN VARCHAR2, p_fieldname IN VARCHAR2, p_value IN VARCHAR2, p_out OUT NUMBER) IS
    BEGIN
        p_out := 0;
        v_sql := 'UPDATE ' || p_table || ' SET ' || p_fieldname || ' = :p_value, ACTUALIZACION = SYSTIMESTAMP WHERE id = :p_id';
        EXECUTE IMMEDIATE v_sql USING p_value, p_id;
        IF sql%rowcount > 0 THEN
            p_out := 1;
            COMMIT;
        END IF;
    EXCEPTION
        WHEN OTHERS THEN
        v_error_code := SQLCODE;
        v_subprogram_name := 'PKG_UTILS.SP_UPDATE_FIELD';
        v_error_message := sqlerrm;
        sp_error_control(v_error_code,v_subprogram_name,v_error_message);
    END SP_UPDATE_FIELD;

END PKG_UTILS;