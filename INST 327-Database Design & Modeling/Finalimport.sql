-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`actors_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`actors_list` (
  `actorID` INT NOT NULL AUTO_INCREMENT,
  `actors` VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (`actorID`),
  UNIQUE INDEX `actorID_UNIQUE` (`actorID` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 432
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`box_office`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`box_office` (
  `boxOfficeID` INT NOT NULL AUTO_INCREMENT,
  `grossIncome` INT UNSIGNED NULL DEFAULT NULL,
  `budget` INT UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`boxOfficeID`))
ENGINE = InnoDB
AUTO_INCREMENT = 432
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`directors_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`directors_list` (
  `directorID` INT NOT NULL AUTO_INCREMENT,
  `directors` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`directorID`),
  UNIQUE INDEX `directorFirstName_UNIQUE` (`directorID` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 432
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`feedback`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`feedback` (
  `feedbackID` INT NOT NULL AUTO_INCREMENT,
  `metascore` INT UNSIGNED NULL DEFAULT NULL,
  `avg_votes` DECIMAL(3,1) UNSIGNED NULL DEFAULT NULL,
  `votes` INT UNSIGNED NULL DEFAULT NULL,
  `userReviews` INT UNSIGNED NULL DEFAULT NULL,
  `criticReviews` INT UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`feedbackID`))
ENGINE = InnoDB
AUTO_INCREMENT = 432
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`production_company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`production_company` (
  `productionID` INT NOT NULL AUTO_INCREMENT,
  `productionName` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`productionID`),
  UNIQUE INDEX `productionID_UNIQUE` (`productionID` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 432
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`writers_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`writers_list` (
  `writerID` INT NOT NULL AUTO_INCREMENT,
  `writers` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`writerID`))
ENGINE = InnoDB
AUTO_INCREMENT = 432
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`general_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`general_information` (
  `movieID` INT NOT NULL AUTO_INCREMENT,
  `movieTitle` VARCHAR(500) NOT NULL,
  `datePublished` DATE NULL DEFAULT NULL,
  `genre` VARCHAR(100) NULL DEFAULT NULL,
  `duration` INT UNSIGNED NULL DEFAULT NULL,
  `directorID` INT NOT NULL,
  `writerID` INT NOT NULL,
  `actorID` INT NOT NULL,
  `productionID` INT NOT NULL,
  `feedbackID` INT NOT NULL,
  `boxOfficeID` INT NOT NULL,
  PRIMARY KEY (`movieID`),
  INDEX `fk_general_information_directors_list1_idx` (`directorID` ASC) VISIBLE,
  INDEX `fk_general_information_writers_list1_idx` (`writerID` ASC) VISIBLE,
  INDEX `fk_general_information_actors_list1_idx` (`actorID` ASC) VISIBLE,
  INDEX `fk_general_information_production_company1_idx` (`productionID` ASC) VISIBLE,
  INDEX `fk_general_information_feedback1_idx` (`feedbackID` ASC) VISIBLE,
  INDEX `fk_general_information_box_office1_idx` (`boxOfficeID` ASC) VISIBLE,
  CONSTRAINT `fk_general_information_actors_list1`
    FOREIGN KEY (`actorID`)
    REFERENCES `mydb`.`actors_list` (`actorID`),
  CONSTRAINT `fk_general_information_box_office1`
    FOREIGN KEY (`boxOfficeID`)
    REFERENCES `mydb`.`box_office` (`boxOfficeID`),
  CONSTRAINT `fk_general_information_directors_list1`
    FOREIGN KEY (`directorID`)
    REFERENCES `mydb`.`directors_list` (`directorID`),
  CONSTRAINT `fk_general_information_feedback1`
    FOREIGN KEY (`feedbackID`)
    REFERENCES `mydb`.`feedback` (`feedbackID`),
  CONSTRAINT `fk_general_information_production_company1`
    FOREIGN KEY (`productionID`)
    REFERENCES `mydb`.`production_company` (`productionID`),
  CONSTRAINT `fk_general_information_writers_list1`
    FOREIGN KEY (`writerID`)
    REFERENCES `mydb`.`writers_list` (`writerID`))
ENGINE = InnoDB
AUTO_INCREMENT = 432
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
