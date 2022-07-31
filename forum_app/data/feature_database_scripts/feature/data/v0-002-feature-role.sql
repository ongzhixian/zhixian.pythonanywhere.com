SET sql_notes = 0; -- suppress warnings

INSERT INTO role (feature_id, name)
SELECT 	id AS 'feature_id'
		, role.name AS 'name' 
FROM 	_feature, 
        (
          	SELECT 			'Feature administrator' AS 'name'
        	UNION SELECT	'Feature user'
		) role
WHERE 	display_name = 'Feature'
;


SET sql_notes = 1; -- enable warnings
