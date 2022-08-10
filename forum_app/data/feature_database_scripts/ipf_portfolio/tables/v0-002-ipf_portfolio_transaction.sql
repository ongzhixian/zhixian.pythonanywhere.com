SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `ipf_portfolio_transaction` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`portfolio_id`			INT UNSIGNED NOT NULL
	`operation`				VARCHAR(10) NULL, -- BUY, SELL, SHORT
	`symbol` 				VARCHAR(50) NULL,
	`quantity` 				DECIMAL NOT NULL,
	`price` 				DECIMAL NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
