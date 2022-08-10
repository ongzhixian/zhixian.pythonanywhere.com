SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `wms_permission_url` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`url` 					VARCHAR(128) NOT NULL,
	`display_text`			VARCHAR(128) NOT NULL,
	`description`			VARCHAR(128) NOT NULL,
	`permission_id`			INT UNSIGNED NULL,
	`display_order`			INT UNSIGNED DEFAULT 1,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `url_u_idx` (`url`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
