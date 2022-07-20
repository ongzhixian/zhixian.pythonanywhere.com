SET sql_notes = 0; -- suppress warnings

-- id, name, isin, code, counter, remarks, type

CREATE TABLE IF NOT EXISTS `asset_class` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 			        VARCHAR(50) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings

-- Seed data
INSERT INTO asset_class(name) VALUES
    (1, 'CASH'),
    (2, 'EQUITY'),
    (3, 'FIXED INCOME'),
    (4, 'FOREIGN CURRENCY')
    (5, 'REAL ESTATE'),
    (6, 'COMMODITY'),
    (7, 'INDEX'),
    
-- Four main types of assets are used for CFD trading 
-- commodities, currency pairs, stocks, and indices

-- The 4 main asset classes used in CFD trading:
-- 1.  COMMODITY
-- 2.  CURRENTCY pairs
-- 3.  Stock
-- 4.  INDEX
-- 5.  BOND 
-- INSERT INTO instrument_type(name) VALUES 
--     ('Stock')
--     , ('REIT')
--     , ('Business Trust')
--     , ('ETF')
--     , ('Structured Warrant')
--     , ('Daily Leverage Certificate')
--     , ('Leveraged & Inverse Product')
--     , ('Company Warrant')
--     , ('ADR');