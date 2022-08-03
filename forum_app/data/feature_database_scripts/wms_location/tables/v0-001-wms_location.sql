SET sql_notes = 0; -- suppress warnings

-- Warehouse -- Addressable
-- Floor
-- Section
-- Shelf
-- Rack
-- Bin

CREATE TABLE IF NOT EXISTS `wms_location` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`location_type_id`		INT UNSIGNED NOT NULL,
	`name` 					VARCHAR(50) NULL,
	`parent_id`				INT UNSIGNED NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_unicode_ci'
;


SET sql_notes = 1; -- enable warnings
