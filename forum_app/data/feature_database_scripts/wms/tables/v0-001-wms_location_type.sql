SET sql_notes = 0; -- suppress warnings

-- Warehouse -- Addressable
-- Floor
-- Section
-- Shelf
-- Rack
-- Bin


CREATE TABLE IF NOT EXISTS `wms_location_type` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(50) NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO `wms_location_type` (`name`) 
	VALUES ('Warehouse'),
		   ('Building'),
		   ('Floor'),
		   ('Section'),
		   ('Room'),
		   ('Shelf'),
		   ('Rack'),
		   ('Bin');


SET sql_notes = 1; -- enable warnings
