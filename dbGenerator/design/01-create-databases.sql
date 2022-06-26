CREATE DATABASE zhixian$forum;
CREATE DATABASE zhixian$default;

CREATE TABLE `login` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(50) NOT NULL,
	`password_hash` VARCHAR(50) NOT NULL,
	`password_salt` VARCHAR(50) NOT NULL,
	`create_dt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`password_update_dt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	`last_login_dt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	UNIQUE INDEX `login_u_idx` (`username`)
)
COLLATE='utf8mb4_unicode_ci'
;


DELIMITER //
CREATE PROCEDURE add_login (
   IN prm_username VARCHAR(50)
)
BEGIN
	INSERT INTO login(
		username
		, password_hash
		, password_salt
	) VALUES (
		prm_username
		, 'test'
		, 'test');
END //

{
	"login": {
		"id": int
	}
}