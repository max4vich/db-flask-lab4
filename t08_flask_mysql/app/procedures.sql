-- Забезпечити параметризовану вставку нових значень у таблицю
DROP PROCEDURE IF EXISTS insert_label;

DELIMITER $$
CREATE PROCEDURE insert_label(
  IN name VARCHAR(255),
  IN country VARCHAR(255)
)
BEGIN
  INSERT INTO `iot_db`.`label`
  (`name`, `country`)
  VALUES
  (name, country);
END $$
DELIMITER ;

-- Використання скрипта
CALL insert_label('Plish Adnrii', 'Україна');
CALL insert_label('Lisnyi Leshyi', 'Україна');



-- Скрипт для створення пакета з 10 рядків
DROP PROCEDURE IF EXISTS insert_rows_into_artists;

DELIMITER $$
CREATE PROCEDURE insert_rows_into_artists()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 10 DO
    INSERT INTO artist (name) VALUES (CONCAT('Artist', i));
    SET i = i + 1;
  END WHILE;
END$$
DELIMITER ;

-- Використання скрипта
CALL insert_rows_into_artists();



-- Скрипт для користувацької функції агрегаційних операцій над duration
DELIMITER //
CREATE FUNCTION GetMaxDuration() RETURNS TIME DETERMINISTIC
BEGIN
    DECLARE max_duration TIME;
    SELECT MAX(duration) INTO max_duration FROM song;
    RETURN max_duration;
END //
DELIMITER ;

-- Використання скрипта
SELECT 
    GetMaxDuration() AS Max_Duration



-- Скрипт з курсором

DELIMITER //
CREATE PROCEDURE ProcCursor()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE NameT CHAR(45);
    DECLARE i INT;

    DECLARE St_Cursor CURSOR FOR SELECT name FROM label;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN St_Cursor;

    myLoop: LOOP
        FETCH St_Cursor INTO NameT;
        IF done = TRUE THEN
            LEAVE myLoop;
        END IF;

        SET @temp_query = CONCAT('CREATE DATABASE `', NameT, '`');
        PREPARE myquery FROM @temp_query;
        EXECUTE myquery;
        DEALLOCATE PREPARE myquery;

        SET i = 1;
        WHILE i <= FLOOR(1 + RAND() * 9) DO
            SET @temp_query = CONCAT('CREATE TABLE `', NameT, '`.`', NameT, i, '` (id INT)');
            PREPARE myquery FROM @temp_query;
            EXECUTE myquery;
            DEALLOCATE PREPARE myquery;
            SET i = i + 1;
        END WHILE;
    END LOOP;

    CLOSE St_Cursor;
END //
DELIMITER ;



-- Скрипт з M:M
DELIMITER //
CREATE PROCEDURE InsertIntoArtistLabel(IN artist_name VARCHAR(45), IN label_name VARCHAR(45))
BEGIN
  DECLARE artist_id INT;
  DECLARE label_id INT;

  SELECT `id` INTO artist_id FROM `iot_db`.`artist` WHERE `name` = artist_name;
  SELECT `id` INTO label_id FROM `iot_db`.`label` WHERE `name` = label_name;

  IF artist_id IS NOT NULL AND label_id IS NOT NULL THEN
    INSERT INTO `iot_db`.`artistlabel` (`artist_id`, `label_id`) VALUES (artist_id, label_id);
  ELSE
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Artist or Label does not exist';
  END IF;
END //
DELIMITER ;




