SET sql_notes = 0; -- suppress warnings

INSERT INTO role (feature_id, name)
SELECT 	id AS 'feature_id'
		, role.name AS 'name' 
FROM 	_feature, 
        (
          	SELECT 			'Database administrator' AS 'name'
        	UNION SELECT	'Database user'
		) role
WHERE 	display_name = 'Database'
;


SET sql_notes = 1; -- enable warnings
