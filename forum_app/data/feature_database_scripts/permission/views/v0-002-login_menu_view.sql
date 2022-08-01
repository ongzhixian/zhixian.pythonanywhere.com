-- List usernames and the menu items that have access to
CREATE OR REPLACE VIEW `login_menu_item_view` AS
SELECT  l.username
		, p.feature_id
		, p.target AS 'menu_display_name'
FROM    login l 
INNER JOIN
		login_role lr
		ON l.id = lr.login_id
INNER JOIN
		role_permission rp
		ON rp.role_id = lr.role_id
INNER JOIN
		permission p
		ON rp.permission_id = p.id
WHERE   p.action = 'View application menu item'
;