SET sql_notes = 0; -- suppress warnings


CREATE TABLE IF NOT EXISTS `wms_supplier` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(50) NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO `wms_supplier` (`name`) 
	VALUES ('Supplier 1'),
		   ('Supplier 2'),
		   ('Supplier 3'),
		   ('Supplier 4'),
		   ('Supplier 5'),
		   ('Supplier 6'),
		   ('Supplier 7'),
		   ('Supplier 8'),
		   ('Supplier 9'),
		   ('Supplier 10');

SET sql_notes = 1; -- enable warnings
