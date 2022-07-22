CREATE OR REPLACE VIEW `feature` AS
SELECT 	 c.id
		, REPLACE(LOWER(c.name), ' ', '-') AS 'name'
        , c.name AS 'display_text'
        , c.description
        , c.module_name
        , COALESCE(p.is_enable, c.is_enable) AS `is_enable`
        , c.parent_id
        , c.apply_dt
FROM 	_feature c
LEFT OUTER JOIN	
		_feature p
		ON c.parent_id = p.id
ORDER BY c.name
;