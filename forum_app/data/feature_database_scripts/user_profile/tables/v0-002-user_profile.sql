SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `user_profile` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`login_id` 				INT UNSIGNED NOT NULL,
	`first_name` 			VARCHAR(128) NOT NULL,
	`last_name` 			VARCHAR(128) NOT NULL,
	`email` 				VARCHAR(128) NOT NULL,
	`portrait_filename`		VARCHAR(128) NULL,
	`background_filename`	VARCHAR(128) NULL,
    `background_position_x`	INT NOT NULL DEFAULT 0,
    `background_position_y`	INT NOT NULL DEFAULT 0,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
