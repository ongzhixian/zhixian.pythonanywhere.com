CREATE OR REPLACE VIEW `feature` AS
SELECT 	REPLACE(LOWER(name), ' ', '-') AS 'name'
		, name AS 'display_text'
        , module_name
        , is_enable
FROM 	_feature
ORDER BY name
;