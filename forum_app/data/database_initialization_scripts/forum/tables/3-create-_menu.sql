SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `_menu` (
	`id`        		INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`display_name`		VARCHAR(128) NOT NULL,
	`href`				VARCHAR(128) NULL,
	`description`		VARCHAR(256) NOT NULL,
	`level`				INT UNSIGNED DEFAULT 0,
	`parent_id`			INT UNSIGNED NULL,
	`ancestor_id`		INT UNSIGNED NULL,
	`display_order`		INT UNSIGNED DEFAULT 0,
	`apply_dt`  		DATETIME NULL DEFAULT NULL,
	`cre_dt`    		DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt`    		DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
) COLLATE='utf8mb4_unicode_ci';


INSERT INTO _menu (display_name, href, description, level, display_order)
VALUES 
    ('Applications', null, 'Applications', 1, 1)
    , ('Administration', null, 'Administration', 1, 2);


INSERT INTO _menu (display_name, href, description, level, parent_id, ancestor_id, display_order)
SELECT  'Database' AS display_name
        , '/database' AS href
        , 'Database module' AS description
        , level + 1 AS level
        , id AS parent_id
        , COALESCE(ancestor_id, id) AS ancestor_id
        , 1 AS display_order
FROM    _menu
WHERE   display_name = 'Administration';

INSERT INTO _menu (display_name, href, description, level, parent_id, ancestor_id, display_order)
SELECT  'Feature' AS display_name
        , '/feature' AS href
        , 'Feature module' AS description
        , level + 1 AS level
        , id AS parent_id
        , COALESCE(ancestor_id, id) AS ancestor_id
        , 2 AS display_order
FROM    _menu
WHERE   display_name = 'Administration';


SET sql_notes = 1; -- enable warnings