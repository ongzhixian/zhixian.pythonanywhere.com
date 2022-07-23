SET sql_notes = 0; -- suppress warnings

-- id, name, isin, code, counter, remarks, type

CREATE TABLE IF NOT EXISTS `development_note` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`route` 			    VARCHAR(128) NOT NULL,
	`content` 			    TEXT NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
