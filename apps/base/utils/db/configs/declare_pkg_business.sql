CREATE OR REPLACE PACKAGE PKG_BUSINESS IS 
   PROCEDURE SP_FINE_VALUE (p_pk check_out.id%type);
   PROCEDURE SP_DF_ML;
END PKG_BUSINESS;
