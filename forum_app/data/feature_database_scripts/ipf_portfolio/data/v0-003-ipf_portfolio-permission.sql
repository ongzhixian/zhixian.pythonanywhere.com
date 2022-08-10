SET sql_notes = 0; -- suppress warnings

INSERT INTO permission (feature_id, action, target)
SELECT 	id AS 'feature_id'
		, permission.action
        , permission.target
FROM   	_feature, 
        (
            SELECT          'View dashboard'            AS 'action', 'IPF Portfolio' AS 'target'
            UNION SELECT    'List'                      AS 'action', 'IPF Portfolio' AS 'target'
            UNION SELECT    'Add'                       AS 'action', 'IPF Portfolio' AS 'target'
            UNION SELECT    'Update'                    AS 'action', 'IPF Portfolio' AS 'target'
            UNION SELECT    'Remove'                    AS 'action', 'IPF Portfolio' AS 'target'
            UNION SELECT    'View'                      AS 'action', 'IPF Portfolio' AS 'target'
		) permission
WHERE 	display_name = 'IPF Portfolio'
;

SET sql_notes = 1; -- enable warnings
