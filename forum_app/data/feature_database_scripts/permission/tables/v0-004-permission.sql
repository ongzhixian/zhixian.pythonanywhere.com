SET sql_notes = 0; -- suppress warnings

CREATE TABLE IF NOT EXISTS `permission` (
	`id`					INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`feature_id` 			INT UNSIGNED NOT NULL,
	`action` 				VARCHAR(50) NOT NULL,
	`target` 				VARCHAR(50) NOT NULL,
	`cre_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`upd_dt` 				DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `feature_action_target_u_idx` (`feature_id`, `action`, `target`)
)
COLLATE='utf8mb4_unicode_ci'
;


-- INSERT INTO role (feature_id, name)
-- SELECT 	id AS 'feature_id'
-- 		, role.name AS 'name' 
-- FROM 	_feature, 
--         (
--           	SELECT 			'Trade administrator' AS 'name'
--         	UNION SELECT	'Trade user'
-- 		) role
-- WHERE 	display_name = 'Trade'
-- ;


-- INSERTs should be defined by the individual features that support permission
-- INSERT INTO permission (action, target) VALUES ('add', 'user');
-- INSERT INTO permission (action, target) VALUES ('update', 'user');
-- INSERT INTO permission (action, target) VALUES ('delete', 'user');
-- INSERT INTO permission (action, target) VALUES ('view', 'user');
-- INSERT INTO permission (action, target) VALUES ('list', 'user');

SET sql_notes = 1; -- enable warnings
