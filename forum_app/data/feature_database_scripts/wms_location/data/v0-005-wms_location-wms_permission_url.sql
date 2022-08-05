SET sql_notes = 0; -- suppress warnings

INSERT INTO `wms_permission_url` (url, display_text, description, display_order, permission_id)
SELECT  '/wms/location/list'            AS 'url'
        , 'Location'                    AS 'display_text'
        , 'Warehouse locations'         AS 'description'
        , 2                             AS 'display_order'
        , p.id                          AS 'permission_id'
FROM    permission p
WHERE   p.action = 'List'
        AND p.target = 'WMS Location'
;

SET sql_notes = 1; -- enable warnings
