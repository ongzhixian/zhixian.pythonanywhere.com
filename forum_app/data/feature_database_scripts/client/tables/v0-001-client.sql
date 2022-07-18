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

INSERT INTO client_type (id, name) VALUES (1, 'Generic'); -- If id is zero, it will use auto-increment unless we SET sql_mode='NO_AUTO_VALUE_ON_ZERO';
INSERT INTO client_type (name) VALUES ('Investment');
INSERT INTO client_type (name) VALUES ('Inventory');

CREATE TABLE IF NOT EXISTS `client` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(64) NOT NULL,
	`type_id` 				INT UNSIGNED NOT NULL DEFAULT 1,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`, `type_id`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO client (name) VALUES ('generic-client 1');
INSERT INTO client (name) VALUES ('generic-client 2');
INSERT INTO client (name) VALUES ('generic-client 3');

SET sql_notes = 1; -- enable warnings
