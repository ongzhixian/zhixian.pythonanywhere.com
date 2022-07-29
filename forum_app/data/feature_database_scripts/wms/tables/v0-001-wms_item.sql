SET sql_notes = 0; -- suppress warnings


CREATE TABLE IF NOT EXISTS `wms_item` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`item_definition_id` 	INT UNSIGNED NOT NULL,
	`name` 					VARCHAR(50) NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;



SET sql_notes = 1; -- enable warnings
