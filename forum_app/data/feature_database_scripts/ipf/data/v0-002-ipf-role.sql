SET sql_notes = 0; -- suppress warnings

INSERT INTO role (feature_id, name)
SELECT 	id AS 'feature_id'
		, role.name AS 'name' 
FROM 	_feature, 
        (
          	SELECT 			'IPF administrator' AS 'name'
        	UNION SELECT	'IPF user'
			UNION SELECT	'IPF customer'
		) role
WHERE 	display_name = 'Investment Portfolio'
;

SET sql_notes = 1; -- enable warnings
