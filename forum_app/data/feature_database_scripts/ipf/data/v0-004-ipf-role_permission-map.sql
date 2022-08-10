SET sql_notes = 0; -- suppress warnings

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'IPF user'
        AND p.action = 'View application menu item'
        AND p.target = 'IPF';

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'IPF administrator'
        AND p.action = 'View application menu item'
        AND p.target = 'IPF';

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'IPF customer'
        AND p.action = 'View application menu item'
        AND p.target = 'IPF';

SET sql_notes = 1; -- enable warnings
