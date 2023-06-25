ALTER TABLE gn_user
    MODIFY COLUMN password_salt varchar(32),
    MODIFY COLUMN password_hash varchar(80);