CREATE OR REPLACE VIEW `role_permission_view` AS
SELECT 	l.username, r.name AS 'role_name'
FROM	login_role lr
JOIN 	login l
		ON lr.login_id = l.id
JOIN 	role r
		ON lr.role_id = r.id
;