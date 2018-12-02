CREATE TABLE `hzs`.`team` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `name` VARCHAR(100) NOT NULL,
 `description` TEXT NULL,
 `photo_url` VARCHAR(45) NULL,
 `team_uuid` VARCHAR(36) NOT NULL,
 PRIMARY KEY (`id`));
