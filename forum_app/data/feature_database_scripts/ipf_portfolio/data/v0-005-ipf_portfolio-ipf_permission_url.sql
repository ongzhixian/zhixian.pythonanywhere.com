SET sql_notes = 0; -- suppress warnings

INSERT INTO `ipf_permission_url` (url, display_text, description, display_order, permission_id)
SELECT  '/ipf/portfolio/list'           AS 'url'
        , 'Investment portfolio'        AS 'display_text'
        , 'Investment portfolios'       AS 'description'
        , 1                             AS 'display_order'
        , p.id                          AS 'permission_id'
FROM    permission p
WHERE   p.action = 'List'
        AND p.target = 'IPF Portfolio'
;

SET sql_notes = 1; -- enable warnings
