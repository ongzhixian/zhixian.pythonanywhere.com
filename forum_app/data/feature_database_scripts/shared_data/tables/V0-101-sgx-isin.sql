SET sql_notes = 0; -- suppress warnings

-- SGX ISIN file is fixed width;
-- 50                                                10        20                  10        30
-- 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
-- NAME                                              STATUS    ISIN CODE           CODE      TRADING COUNTER NAME
-- Note: ISIN CODE is the ISIN code of the security; CODE is the trading counter code; TRADING COUNTER NAME is the name of the trading counter.
-- 		 SGX ISIN file is fixed width;
-- 		 ISIN maybe repeated in the file; 
-- example AEM Holdings (same ISIN: SG1BA1000003) has 2 codes AWX and XWA  (because it support dual-currency trading)
-- See https://sg.finance.yahoo.com/news/aem-commence-dual-currency-trading-225613210.html
-- AWX => AEM SGD (AWX / AEM.SI)
-- XWA => AEM USD (XWA / AEM.SI)

CREATE TABLE IF NOT EXISTS `isin` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` 			        VARCHAR(50) NOT NULL,
	`isin` 				    VARCHAR(20) NOT NULL,
	`code` 				    VARCHAR(10) NOT NULL,
    `counter_name`          VARCHAR(30) NOT NULL,
    `status`                VARCHAR(10) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `code_u_idx` (`code`)
)
COLLATE='utf8mb4_unicode_ci'
;

SET sql_notes = 1; -- enable warnings
