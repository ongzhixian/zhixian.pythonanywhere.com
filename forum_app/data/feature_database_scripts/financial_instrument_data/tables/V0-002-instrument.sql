SET sql_notes = 0; -- suppress warnings

-- id, name, isin, code, counter, remarks, type

CREATE TABLE IF NOT EXISTS `instrument` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 			        VARCHAR(50) NOT NULL,
	`isin` 				    VARCHAR(20) NOT NULL,
	-- `sedol` 				VARCHAR(20) NOT NULL,
	-- `cusip` 				VARCHAR(20) NOT NULL,
	-- `wkn` 				    VARCHAR(20) NOT NULL,
	`mic` 				    VARCHAR(4) NOT NULL,
    `ticker`				VARCHAR(10) NOT NULL, -- AKA counter / symbol
	`ticker_name`          	VARCHAR(30) NOT NULL,
    `remarks`               VARCHAR(10) NOT NULL,
	`type_id`               INT UNSIGNED NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
	-- , FOREIGN KEY (type_id) REFERENCES instrument_type(id)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings

