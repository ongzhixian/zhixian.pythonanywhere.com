SET sql_notes = 0; -- suppress warnings

INSERT INTO permission (feature_id, action, target)
SELECT 	id AS 'feature_id'
		, permission.action
        , permission.target
FROM   	_feature, 
        (
            SELECT 			'View' AS 'action', 'Trade application menu item' AS 'target'
		) permission
WHERE 	display_name = 'Trade'
;

SET sql_notes = 1; -- enable warnings
