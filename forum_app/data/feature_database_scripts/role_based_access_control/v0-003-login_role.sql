SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `login_role` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`login_id` 				INT UNSIGNED NOT NULL,
	`role_id` 				INT UNSIGNED NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `login_role_u_idx` (`login_id`, `role_id`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
