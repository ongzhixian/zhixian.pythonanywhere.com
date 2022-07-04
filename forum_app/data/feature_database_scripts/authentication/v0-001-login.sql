SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `login` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`username` 				VARCHAR(50) NOT NULL,
	`password_hash` 		VARCHAR(128) NOT NULL,
	`password_salt` 		VARCHAR(32) NOT NULL,
	`password_update_dt` 	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`last_login_dt` 		DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `login_u_idx` (`username`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
