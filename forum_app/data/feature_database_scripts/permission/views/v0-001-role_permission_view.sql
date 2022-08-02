CREATE OR REPLACE VIEW `role_permission_view` AS
SELECT 	r.name AS 'role_name'
        , p.action AS 'action'
        , p.target AS 'target'
FROM	role_permission rp
JOIN 	role r
		ON rp.role_id = r.id
JOIN 	permission p
		ON rp.permission_id = p.id
;