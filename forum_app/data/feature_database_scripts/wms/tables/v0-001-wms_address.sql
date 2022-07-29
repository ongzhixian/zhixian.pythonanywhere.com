SET sql_notes = 0; -- suppress warnings

-- country
-- sector / state
-- city
-- address1
-- address2
-- postcode

CREATE TABLE IF NOT EXISTS `wms_address` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`country` 				VARCHAR(128) NULL,
	`sector` 				VARCHAR(128) NULL,
	`city` 					VARCHAR(128) NULL,
	`address1` 				VARCHAR(128) NULL,
	`address2` 				VARCHAR(128) NULL,
	`postcode` 				VARCHAR(50) NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
