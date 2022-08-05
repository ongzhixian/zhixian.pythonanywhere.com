SET sql_notes = 0; -- suppress warnings

INSERT INTO `wms_permission_url` (url, display_text, description, display_order, permission_id)
SELECT  '/wms/location-type/list'       AS 'url'
        , 'Location type'               AS 'display_text'
        , 'Warehouse location types'    AS 'description'
        , 1                             AS 'display_order'
        , p.id                          AS 'permission_id'
FROM    permission p
WHERE   p.action = 'List'
        AND p.target = 'WMS Location Type'
;

SET sql_notes = 1; -- enable warnings
