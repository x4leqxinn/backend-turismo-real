CREATE OR REPLACE TRIGGER trg_login_session
AFTER LOGON ON DATABASE
BEGIN
------------------------------------------------------------------------------
-- FORMATO ZONA HORARIA SANTIAGO CHILE
------------------------------------------------------------------------------
    EXECUTE IMMEDIATE 'ALTER SESSION SET NLS_DATE_FORMAT=''DD-MM-YYYY''';
    -- Indicamos el lenguaje
    EXECUTE IMMEDIATE 'ALTER SESSION SET  NLS_DATE_LANGUAGE=''SPANISH''';
    -- Indicamos la zona horaria America
    EXECUTE IMMEDIATE 'ALTER SESSION SET NLS_TERRITORY = "CHILE"';
END trg_login_session;
