SET sql_notes = 0; -- suppress warnings


-- Sample data: ('XAG_USD', 'Silver', 'METAL', 'COMMODITY', 'METAL')
-- ticker, name, type, asset_class, kid_assets_class
-- Note-1: ignoring kid_assets_class for now since its currently used only for metals
-- Note-2: Yes, using varchar for type_id, asset_class, and execution_venue is terrible; KIV until we add other markets
-- Note-3: Possible naming for a Execution venue identifier code ('evic'?)

CREATE TABLE IF NOT EXISTS `trade_instrument` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 			        VARCHAR(50) NOT NULL,
    `ticker` 			    VARCHAR(10) NOT NULL,
    `type_id` 			    VARCHAR(50) NOT NULL,
    `asset_class` 			VARCHAR(50) NOT NULL,
    `execution_venue` 		VARCHAR(50) NOT NULL,
	`is_tradable` 			BOOLEAN NOT NULL DEFAULT TRUE,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name_u_idx` (`name`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
