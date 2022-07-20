SET sql_notes = 0; -- suppress warnings

-- id, name, isin, code, counter, remarks, type

CREATE TABLE IF NOT EXISTS `instrument` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 			        VARCHAR(50) NOT NULL,
	`isin` 				    VARCHAR(20) NULL,
	`valor` 			    VARCHAR(20) NULL,
	`sedol` 				VARCHAR(20) NULL,
	`cusip` 				VARCHAR(20) NULL,
	`wkn` 				    VARCHAR(20) NULL, -- WKN, or Wertpapierkennnummer, (WKN, WPKN, WPK or simply Wert),
	`mic` 				    VARCHAR(04) NULL,
    `ticker`				VARCHAR(10) NULL, -- AKA counter / symbol
	`ticker_name`          	VARCHAR(30) NULL,
	`currency` 			    VARCHAR(03) NULL, -- Trading currency, ISO 4217
    `remarks`               VARCHAR(10) NOT NULL DEFAULT '',
	`type_id`               INT UNSIGNED NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
	-- , FOREIGN KEY (type_id) REFERENCES instrument_type(id)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings

