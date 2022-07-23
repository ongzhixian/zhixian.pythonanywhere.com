SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `permission` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`action` 				VARCHAR(50) NOT NULL,
	`target` 				VARCHAR(50) NOT NULL, 
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `action_u_idx` (`name`, `entity`)
)
COLLATE='utf8mb4_unicode_ci'
;

-- INSERTs should be defined by the individual features that support permission
-- INSERT INTO permission (action, target) VALUES ('add', 'user');
-- INSERT INTO permission (action, target) VALUES ('update', 'user');
-- INSERT INTO permission (action, target) VALUES ('delete', 'user');
-- INSERT INTO permission (action, target) VALUES ('view', 'user');
-- INSERT INTO permission (action, target) VALUES ('list', 'user');

SET sql_notes = 1; -- enable warnings
