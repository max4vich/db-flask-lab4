-- Забезпечити параметризовану вставку нових значень у таблицю
-- Скрипт
DROP PROCEDURE IF EXISTS insert_label;

DELIMITER $$

CREATE PROCEDURE insert_label(
  IN name VARCHAR(255),
  IN country VARCHAR(255)
)
BEGIN

  -- Вставка нового рядка
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
DROP PROCEDURE IF EXISTS InsertRows;
DELIMITER $$
CREATE PROCEDURE InsertRows()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 10 DO
    INSERT INTO artist (name) VALUES (CONCAT('Artist', i));
    SET i = i + 1;
  END WHILE;
END$$
DELIMITER ;

CALL InsertRows();

-- Використання пакета
CALL insert_multiple_strings('album');



-- Скрипт для агрегаційних операцій над duration
DELIMITER //

CREATE PROCEDURE GetDurationStats()
BEGIN
    DECLARE max_duration TIME;
    DECLARE min_duration TIME;
    DECLARE total_duration TIME;
    DECLARE avg_duration TIME;
    DECLARE song_count INT;

    SELECT MAX(duration) INTO max_duration FROM song;
    SELECT MIN(duration) INTO min_duration FROM song;
    SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(duration))) INTO total_duration FROM song;
    SELECT SEC_TO_TIME(AVG(TIME_TO_SEC(duration))) INTO avg_duration FROM song;
    SELECT COUNT(*) INTO song_count FROM song;
	
    SELECT 
        max_duration AS Max_Duration,
        min_duration AS Min_Duration,
        total_duration AS Total_Duration,
        avg_duration AS Avg_Duration,
        song_count AS Song_Count;
END //

DELIMITER ;

-- Використання скрипта
CALL GetDurationStats();

