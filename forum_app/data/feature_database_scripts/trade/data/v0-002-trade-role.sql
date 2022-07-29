SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `role` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(50) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO `role` (`name`) VALUES ('Trade administrator');
INSERT INTO `role` (`name`) VALUES ('Trade user');

SET sql_notes = 1; -- enable warnings
