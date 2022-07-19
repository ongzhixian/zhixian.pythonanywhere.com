SET sql_notes = 0; -- suppress warnings

-- NOTE: Market Identifier Code (MIC)

CREATE TABLE IF NOT EXISTS `market_identifier` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`country_name` 			VARCHAR(60) NOT NULL,
	`country_code2`			VARCHAR(2) NOT NULL,
	`code` 					VARCHAR(4) NOT NULL,
	`operating_mic`			VARCHAR(4) NOT NULL,
	`name` 					VARCHAR(110) NOT NULL,
	`short_name`			VARCHAR(60) NULL,
	`city`					VARCHAR(60) NULL,
	`url`					VARCHAR(128) NULL,
	`status`				VARCHAR(10) NULL,
	`comments`				VARCHAR(255) NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `country_name_u_idx` (`country_name`, `code`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
