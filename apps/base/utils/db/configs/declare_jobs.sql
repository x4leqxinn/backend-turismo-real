BEGIN
    -- JOB QUE SE EJECUTA CADA MES Y AGREGA INFORMACIÓN AL DATAFRAME
    dbms_scheduler.create_job (
    job_name          =>  'JOB_MACHINE_LEARNING', 
    job_type            =>  'STORED_PROCEDURE',
    job_action          =>  'PKG_BUSINESS.SP_DF_ML', 
    start_date          =>  NULL, 
    repeat_interval  => 'freq=monthly;bymonthday=1;byhour=01;byminute=01;bysecond=01', 
    enabled             =>  TRUE);
END;
