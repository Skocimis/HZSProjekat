CREATE TABLE `hzs`.`team_member` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(80) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `phone_number` VARCHAR(20) NULL,
  `school` VARCHAR(100) NULL,
  `city` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
