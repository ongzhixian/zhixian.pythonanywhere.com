SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `action` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`verb` 					VARCHAR(50) NOT NULL,
	`entity` 				VARCHAR(50) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `action_u_idx` (`verb`, `entity`)
)
COLLATE='utf8mb4_unicode_ci'
;

CREATE TABLE IF NOT EXISTS `role_action` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`role_id` 				INT UNSIGNED NOT NULL,
	`action_id` 			INT UNSIGNED NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `role_action_u_idx` (`role_id`, `action_id`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO action (verb, entity) VALUES ('add', 'user');
INSERT INTO action (verb, entity) VALUES ('update', 'user');
INSERT INTO action (verb, entity) VALUES ('delete', 'user');
INSERT INTO action (verb, entity) VALUES ('view', 'user');
INSERT INTO action (verb, entity) VALUES ('list', 'user');

SET sql_notes = 1; -- enable warnings
