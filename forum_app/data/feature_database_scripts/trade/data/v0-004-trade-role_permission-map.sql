SET sql_notes = 0; -- suppress warnings

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'Trade user'
        AND p.action = 'View application menu item'
        AND p.target = 'Trade';

SET sql_notes = 1; -- enable warnings
