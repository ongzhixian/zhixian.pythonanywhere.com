SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `_feature` (
	`id`        		INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name`   			VARCHAR(128) NOT NULL,
	`display_name`		VARCHAR(128) NOT NULL,
	`description`		VARCHAR(256) NOT NULL,
	`module_name`		VARCHAR(128) NOT NULL,
	`is_enable`			BOOLEAN NOT NULL DEFAULT FALSE,
	`level`				INT UNSIGNED NOT NULL,
	`parent_id`			INT UNSIGNED NULL,
	`ancestor_id`		INT UNSIGNED NULL,
	`cre_dt`    		DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt`    		DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
) COLLATE='utf8mb4_unicode_ci';

-- ALTER TABLE `_feature`
--     ADD COLUMN `has_api` 		BOOLEAN NOT NULL DEFAULT FALSE,
--     ADD COLUMN `has_pages` 		BOOLEAN NOT NULL DEFAULT FALSE,
--     ADD COLUMN `template_path`	VARCHAR(128) NOT NULL DEFAULT '';
	
SET sql_notes = 1; -- enable warnings