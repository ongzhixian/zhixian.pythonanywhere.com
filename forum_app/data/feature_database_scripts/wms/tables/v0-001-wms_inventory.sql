SET sql_notes = 0; -- suppress warnings


CREATE TABLE IF NOT EXISTS `wms_inventory` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(50) NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO `wms_inventory` (`name`) 
	VALUES ('Item 1'),
		   ('Item 2'),
		   ('Item 3'),
		   ('Item 4'),
		   ('Item 5'),
		   ('Item 6'),
		   ('Item 7'),
		   ('Item 8'),
		   ('Item 9'),
		   ('Item 10');

SET sql_notes = 1; -- enable warnings
