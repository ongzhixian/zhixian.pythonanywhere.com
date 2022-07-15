SET sql_notes = 0; -- suppress warnings

-- Note: Some countries have multiple currencies (example: Bhutan).
-- KIV: is_fund (boolean)

CREATE TABLE IF NOT EXISTS `currency` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`country_name` 			VARCHAR(60) NOT NULL,
	`name`					VARCHAR(70) NOT NULL,
	`code` 					VARCHAR(3) NULL,
	`number` 				INT NULL,
	`minor_unit`			INT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `country_name_u_idx` (`country_name`, `code`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
