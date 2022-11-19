
-- PACKAGE DE UTILIDADES
CREATE OR REPLACE PACKAGE PKG_UTILS IS
    -- SQL Dinámico 
    V_SQL VARCHAR2(1000);
    
    -- Mensajes de error 
    v_error_message ERROR_PROCESO.MENSAJE_ERROR%TYPE;
    
    -- Códigos de error
    v_error_code ERROR_PROCESO.COD_ERROR%TYPE;
    
    -- Nombre subprograma
    v_subprogram_name ERROR_PROCESO.SUBPROGRAMA%TYPE;
    
    -- Valor Secuencia
    v_seq_val number(20);

    -- CONTROL DE ERRORES
    PROCEDURE SP_ERROR_CONTROL(p_cod_error ERROR_PROCESO.COD_ERROR%TYPE, p_subprogram ERROR_PROCESO.SUBPROGRAMA%TYPE, p_message ERROR_PROCESO.MENSAJE_ERROR%TYPE);
    
    -- CALCULAR EDAD
    FUNCTION FN_GET_AGE(p_birthday DATE) RETURN NUMBER;
    
    -- ELIMINACIÓN LÓGICA
    PROCEDURE SP_DELETE_ENTITY(p_id IN NUMBER, p_table IN VARCHAR2, p_out OUT NUMBER);
    
    -- CAMBIAR ESTADO
    PROCEDURE SP_CHANGE_STATE_ENTITY(p_id IN NUMBER, p_table IN VARCHAR2, p_state IN VARCHAR2, p_out OUT NUMBER);

    -- ACTUALIZAR GÉNERICO
    PROCEDURE SP_UPDATE_FIELD(p_id IN NUMBER, p_table IN VARCHAR2, p_fieldname IN VARCHAR2, p_value IN VARCHAR2, p_out OUT NUMBER);
    
    -- TRUNCA TABLAS
    PROCEDURE SP_TRUNCATE_TABLE(p_table_name IN VARCHAR2);

    -- ELIMINA TABLAS DE LA BASE DE DATOS
    PROCEDURE SP_DROP_TABLES;

END PKG_UTILS;