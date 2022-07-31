SET sql_notes = 0; -- suppress warnings

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'Feature user'
        AND p.action = 'View application menu item'
        AND p.target = 'Feature';

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'Feature administrator'
        AND p.action = 'View application menu item'
        AND p.target = 'Feature';

SET sql_notes = 1; -- enable warnings
