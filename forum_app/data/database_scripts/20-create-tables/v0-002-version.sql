SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `_version` (
	`id`        INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`version`   VARCHAR(50) NOT NULL,
	`apply_dt`  DATETIME NULL DEFAULT NULL,
	`cre_dt`    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt`    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
