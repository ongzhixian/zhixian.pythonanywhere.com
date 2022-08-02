SET sql_notes = 0; -- suppress warnings

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'WMS user'
        AND p.action = 'View application menu item'
        AND p.target = 'WMS';

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'WMS administrator'
        AND p.action = 'View application menu item'
        AND p.target = 'WMS';

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'WMS customer'
        AND p.action = 'View application menu item'
        AND p.target = 'WMS';

SET sql_notes = 1; -- enable warnings
