SET sql_notes = 0; -- suppress warnings

INSERT INTO role (feature_id, name)
SELECT 	id AS 'feature_id'
		, role.name AS 'name' 
FROM 	_feature, 
        (
          	SELECT 			'Trade administrator' AS 'name'
        	UNION SELECT	'Trade user'
		) role
WHERE 	display_name = 'Trade'
;


SET sql_notes = 1; -- enable warnings
