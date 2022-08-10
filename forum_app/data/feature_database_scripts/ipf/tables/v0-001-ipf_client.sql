SET sql_notes = 0; -- suppress warnings


CREATE TABLE IF NOT EXISTS `ipf_client` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 					VARCHAR(50) NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

INSERT INTO `ipf_client` (`name`) 
	VALUES 
	('Customer 1'),
	('Customer 2'),
	('Customer 3'),
	('Customer 4');
	
SET sql_notes = 1; -- enable warnings
