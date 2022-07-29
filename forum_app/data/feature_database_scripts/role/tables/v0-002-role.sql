SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `role` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`feature_id` 			INT UNSIGNED NOT NULL,
	`name` 					VARCHAR(50) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO role (feature_id, name)
SELECT 	id AS 'feature_id'
		, 'System administrator' AS 'name' 
FROM 	_feature 
WHERE 	display_name = 'Login'
;

SET sql_notes = 1; -- enable warnings
