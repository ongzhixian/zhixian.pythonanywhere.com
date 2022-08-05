SET sql_notes = 0; -- suppress warnings

INSERT INTO `wms_location_type` (`name`)
    VALUES  ('Warehouse')
            , ('Building')
            , ('Floor')
            , ('Section')
            , ('Room')
            , ('Shelf')
            , ('Rack')
            , ('Bin');

SET sql_notes = 1; -- enable warnings
