SET sql_notes = 0; -- suppress warnings

INSERT INTO role (feature_id, name)
SELECT 	id AS 'feature_id'
		, role.name AS 'name' 
FROM 	_feature, 
        (
          	SELECT 			'WMS administrator' AS 'name'
        	UNION SELECT	'WMS user'
			UNION SELECT	'WMS customer'
		) role
WHERE 	display_name = 'Warehouse Management System'
;

SET sql_notes = 1; -- enable warnings
