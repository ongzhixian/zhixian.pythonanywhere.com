SET sql_notes = 0; -- suppress warnings


-- CREATE TABLE IF NOT EXISTS `wms_item` (
-- 	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
-- 	`item_definition_id` 	INT UNSIGNED NOT NULL,
-- 	`name` 					VARCHAR(50) NULL,
-- 	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
-- 	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
-- 	PRIMARY KEY (`id`),
-- 	UNIQUE INDEX `name_u_idx` (`name`)
-- )
-- COLLATE='utf8mb4_unicode_ci'
-- ;

CREATE TABLE IF NOT EXISTS `wms_item` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`supplier_id` 			INT UNSIGNED NOT NULL,
	`name` 					VARCHAR(50) NULL,
	`description`			VARCHAR(128) NULL,
	`unit_definition_id`	INT UNSIGNED NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;


INSERT INTO `wms_item` (`supplier_id`, `name`, `description`) 
	VALUES (1, 'H8PGN', 'DIMM,8GB,2133,2RX8,4G,DDR4,R'),
		   (1, '1R8CR', 'DIMM,16GB,2133,2RX4,4G,DDR4,R'),
		   (1, 'Y8R2G', 'DIMM,4GB,2133,1RX8,4G,DDR4,R')
		   ;


SET sql_notes = 1; -- enable warnings
