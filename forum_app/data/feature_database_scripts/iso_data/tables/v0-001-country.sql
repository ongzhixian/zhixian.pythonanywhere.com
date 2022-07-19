SET sql_notes = 0; -- suppress warnings

-- English short name,French short name,Alpha-2 code,Alpha-3 code,Numeric

CREATE TABLE IF NOT EXISTS `country` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`short_name` 			VARCHAR(60) NOT NULL,
	`code2` 				VARCHAR(2) NOT NULL,
	`code3` 				VARCHAR(3) NOT NULL,
	`m49` 					INT NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `code2_u_idx` (`code2`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
