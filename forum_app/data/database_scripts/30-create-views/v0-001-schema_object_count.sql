CREATE OR REPLACE VIEW `schema_object_count` AS
SELECT    CAST(SUM(CASE WHEN t.type = 'BASE TABLE' 	THEN 1 ELSE 0 END) AS UNSIGNED) AS 'table_count'
        , CAST(SUM(CASE WHEN t.type = 'VIEW'        THEN 1 ELSE 0 END) AS UNSIGNED) AS 'view_count'
        , CAST(SUM(CASE WHEN t.type = 'PROCEDURE' 	THEN 1 ELSE 0 END) AS UNSIGNED) AS 'procedure_count'
        , CAST(SUM(CASE WHEN t.type = 'FUNCTION' 	THEN 1 ELSE 0 END) AS UNSIGNED) AS 'function_count'
FROM	(
            SELECT  TABLE_TYPE AS 'type', TABLE_NAME AS 'name'
            FROM 	INFORMATION_SCHEMA.TABLES t
            WHERE 	TABLE_SCHEMA = 'forum'
            UNION
            SELECT 	ROUTINE_TYPE, ROUTINE_NAME 
            FROM 	INFORMATION_SCHEMA.ROUTINES r
            WHERE 	ROUTINE_SCHEMA = 'forum'
        ) t;