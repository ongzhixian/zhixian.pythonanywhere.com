SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `wms_unit_definition` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`supplier_id` 			INT UNSIGNED NOT NULL,
	`name` 					VARCHAR(50) NULL,
	`description`			VARCHAR(128) NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO `wms_unit_definition` (`supplier_id`, `name`, `description`) 
	VALUES (1, 'PC', 'Piece'),
		   (1, '10PC/BX', '10 piece per box')
		   ;


SET sql_notes = 1; -- enable warnings
