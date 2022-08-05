SET sql_notes = 0; -- suppress warnings

-- WMS administrator should be able to do everything in location module.

INSERT INTO role_permission (role_id, permission_id)
SELECT  r.id, p.id 
FROM    role r,
        permission p
WHERE   r.name = 'WMS administrator'
        AND p.target = 'WMS Location Type'
;
        

SET sql_notes = 1; -- enable warnings
