SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `trading_api_access_type` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(50) NOT NULL,
	`key`					BOOLEAN NOT NULL DEFAULT 0,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `login_u_idx` (`username`)
)
COLLATE='utf8mb4_unicode_ci'
;


CREATE TABLE IF NOT EXISTS `trading_account_type` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(50) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `login_u_idx` (`username`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO client_type (name) VALUES ('Oanda (Paper)', 1);

CREATE TABLE IF NOT EXISTS `trading_account` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(50) NOT NULL,
	`type_id` 				INT UNSIGNED NOT NULL,
	``
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `login_u_idx` (`username`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
