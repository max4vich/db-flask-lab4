-- Create Trigger to check if device_id exists in device table before inserting into device_info table

DROP TRIGGER IF EXISTS before_insert_device_info;
DROP TRIGGER IF EXISTS names_trigger_for_device;
DROP TRIGGER IF EXISTS block_access_for_deleting_strings;
DROP TRIGGER IF EXISTS block_access_for_modifying;

DELIMITER //
CREATE TRIGGER before_insert_device_info
BEFORE INSERT ON device_info FOR EACH ROW
BEGIN
    DECLARE device_exists INT;
    SELECT COUNT(*) INTO device_exists FROM device WHERE id = NEW.device_id;
    IF device_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Device does not exist in the device table';
    END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER names_trigger_for_device
BEFORE INSERT ON device for EACH ROW
BEGIN 
	IF NOT (NEW.device_type IN ("pc","laptop", "phone")) THEN
    signal sqlstate '45000'
    SET message_text = "Set a correct value";
    end if;
    END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER block_access_for_deleting_strings
BEFORE DELETE ON iot_db.user
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deleting rows from the user table is not allowed';
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER block_access_for_modifying
BEFORE UPDATE ON iot_db.artist
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modifying rows in the artist table is not allowed';
END;
//
DELIMITER ;

    