CREATE TABLE `gn_company` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NOT NULL,
    `cre_dt` date NOT NULL,
    `cre_id` int NOT NULL,
    `upd_dt` date NOT NULL,
    `upd_id` int NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `gn_user` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NOT NULL,
    `first_name` varchar(50) NOT NULL,
    `last_name` varchar(50) NOT NULL,
    `password_salt` varchar(32) NOT NULL,
    `password_hash` varchar(80) NOT NULL,
    `cre_dt` date NOT NULL,
    `cre_id` int NOT NULL,
    `upd_dt` date NOT NULL,
    `upd_id` int NOT NULL,
    PRIMARY KEY (`id`)
);


ALTER TABLE gn_user
    MODIFY COLUMN password_salt varchar(32),
    MODIFY COLUMN password_hash varchar(80);
