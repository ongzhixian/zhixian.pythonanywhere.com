SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `client_type` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(64) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO client_type (id, name) VALUES (0, 'GENERIC');

CREATE TABLE IF NOT EXISTS `client` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(64) NOT NULL,
	`type_id` 				INT UNSIGNED NOT NULL DEFAULT 0,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`, `type_id`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO client (name) VALUES ('test-client 1');
INSERT INTO client (name) VALUES ('test-client 2');
INSERT INTO client (name) VALUES ('test-client 3');

SET sql_notes = 1; -- enable warnings
