SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `client` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`first_name` 			VARCHAR(50) NOT NULL,
	`last_name` 			VARCHAR(50) NOT NULL,
	`domicile_country_id`	VARCHAR(32) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `login_u_idx` (`username`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
