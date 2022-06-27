SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `_feature` (
	`id`        INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name`   	VARCHAR(128) NOT NULL,
	`is_active`	BOOLEAN NOT NULL DEFAULT FALSE,
	`apply_dt`  DATETIME NULL DEFAULT NULL,
	`cre_dt`    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt`    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings