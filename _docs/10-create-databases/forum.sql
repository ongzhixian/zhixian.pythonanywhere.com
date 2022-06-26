SET sql_notes = 0; -- suppress warnings

CREATE DATABASE IF NOT EXISTS forum
CHARACTER SET utf8mb4
COLLATE UTF8MB4_UNICODE_CI;

USE forum;

SELECT DATABASE() AS 'DatabaseName';

SELECT  @@character_set_database
        , @@collation_database;

SET sql_notes = 1; -- enable warnings
