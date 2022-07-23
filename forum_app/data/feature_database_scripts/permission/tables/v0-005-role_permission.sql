SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `role_permission` (
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

SET sql_notes = 1; -- enable warnings
