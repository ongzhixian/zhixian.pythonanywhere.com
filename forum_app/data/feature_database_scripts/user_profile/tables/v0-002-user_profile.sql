SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `user_profile` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`login_id` 				VARCHAR(50) NOT NULL,
	`first_name` 			VARCHAR(128) NOT NULL,
	`last_name` 			VARCHAR(128) NOT NULL,
	`email` 				VARCHAR(128) NOT NULL,
	`portrait_filename`		VARCHAR(128) NOT NULL,
	`background_filename`	VARCHAR(128) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
