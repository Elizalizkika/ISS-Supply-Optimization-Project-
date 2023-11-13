CREATE DATABASE ISSConsumables;
Use ISSConsumables;


CREATE TABLE
    `us_water_use` (
        `Date` date NOT NULL,
        `Corrected_Potable` decimal(10, 2) DEFAULT NULL,
        `Corrected_Technical` decimal(10, 2) DEFAULT NULL,
        `Corrected_Total` decimal(10, 2) DEFAULT NULL,
        `Resupply_Potable` decimal(10, 2) DEFAULT NULL,
        `Resupply_Technical` decimal(10, 2) DEFAULT NULL,
        `Corrected_Predicted` decimal(10, 2) DEFAULT NULL,
        PRIMARY KEY (`Date`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci


CREATE TABLE
    `russian_water_use` (
        `Report_Date` date NOT NULL,
        `Remain_Potable` decimal(10, 2) DEFAULT NULL,
        `Remain_Technical` decimal(10, 2) DEFAULT NULL,
        `Remain_Rodnik` decimal(10, 2) DEFAULT NULL,
        PRIMARY KEY (`Report_Date`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci


CREATE TABLE
    `iss_flight_plan` (
        `datedim` date DEFAULT NULL,
        `vehicle_name` varchar(255) DEFAULT NULL,
        `port_name` varchar(255) DEFAULT NULL,
        `vehicle_type` varchar(255) DEFAULT NULL,
        `eva_name` varchar(255) DEFAULT NULL,
        `eva_type` varchar(50) DEFAULT NULL,
        `eva_accuracy` varchar(50) DEFAULT NULL,
        `event` varchar(50) DEFAULT NULL
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci
	
	
CREATE TABLE
    `gas_consumption` (
        `Date` date DEFAULT NULL,
        `USOS_O2_kg` float DEFAULT NULL,
        `RS_O2_kg` float DEFAULT NULL,
        `US_N2_kg` float DEFAULT NULL,
        `RS_N2_kg` float DEFAULT NULL,
        `Adjusted_O2_kg` float DEFAULT NULL,
        `Adjusted_N2_kg` float DEFAULT NULL,
        `Resupply_O2_kg` float DEFAULT NULL,
        `Resupply_N2_kg` float DEFAULT NULL,
        `Resupply_Air_kg` float DEFAULT NULL
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci


CREATE TABLE
    `crew_flight_plan` (
        `datedim` date DEFAULT NULL,
        `nationality_category` varchar(255) DEFAULT NULL,
        `crew_count` int(11) DEFAULT NULL
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci
	
	
CREATE TABLE
    `consumable_stored_items` (
        `_record_number` int(11) NOT NULL AUTO_INCREMENT,
        `datedim` datetime DEFAULT NULL,
        `id` int(11) DEFAULT NULL,
        `id_parent` int(11) DEFAULT NULL,
        `id_path` varchar(73) DEFAULT NULL,
        `tree_depth` int(11) DEFAULT NULL,
        `tree` varchar(16) DEFAULT NULL,
        `part_number` varchar(18) DEFAULT NULL,
        `serial_number` varchar(14) DEFAULT NULL,
        `location_name` varchar(30) DEFAULT NULL,
        `original_ip_owner` varchar(20) DEFAULT NULL,
        `current_ip_owner` varchar(5) DEFAULT NULL,
        `operational_nomenclature` varchar(28) DEFAULT NULL,
        `russian_name` varchar(46) DEFAULT NULL,
        `english_name` varchar(30) DEFAULT NULL,
        `barcode` varchar(9) DEFAULT NULL,
        `quantity` int(11) DEFAULT NULL,
        `width` decimal(6, 2) DEFAULT NULL,
        `height` decimal(7, 3) DEFAULT NULL,
        `length` decimal(7, 3) DEFAULT NULL,
        `diameter` decimal(5, 2) DEFAULT NULL,
        `calculated_volume` decimal(7, 5) DEFAULT NULL,
        `stwg_ovrrd_vol` varchar(10) DEFAULT NULL,
        `children_volume` decimal(7, 5) DEFAULT NULL,
        `stwg_ovrrd_chldrn_vol` varchar(10) DEFAULT NULL,
        `ovrrd_notes` varchar(10) DEFAULT NULL,
        `volume_notes` varchar(69) DEFAULT NULL,
        `expire_date` datetime DEFAULT NULL,
        `launch` varchar(20) DEFAULT NULL,
        `type` varchar(4) DEFAULT NULL,
        `hazard` varchar(13) DEFAULT NULL,
        `state` varchar(10) DEFAULT NULL,
        `status` varchar(9) DEFAULT NULL,
        `is_container` int(11) DEFAULT NULL,
        `is_moveable` int(11) DEFAULT NULL,
        `What_System` varchar(29) DEFAULT NULL,
        `subsystem` varchar(4) DEFAULT NULL,
        `action_date` datetime DEFAULT NULL,
        `move_date` datetime DEFAULT NULL,
        `fill_status` varchar(5) DEFAULT NULL,
        `categoryID` int(11) DEFAULT NULL,
        `category_name` varchar(14) DEFAULT NULL,
        PRIMARY KEY (`_record_number`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 533988 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci
	
	

CREATE TABLE 
	users (
		Username VARCHAR(255) PRIMARY KEY,
		Email VARCHAR(255) NOT NULL,
		FirstName VARCHAR(255) NOT NULL,
		LastName VARCHAR(255) NOT NULL,
		Permissions VARCHAR(255)
		-- FOREIGN KEY (Permissions) REFERENCES permissions(PermissionLevel)
);

ALTER TABLE users
ADD FOREIGN KEY (Permissions) REFERENCES permissions(PermissionLevel);

CREATE TABLE 
	passwords (
		Username VARCHAR(255) PRIMARY KEY,
		Password VARCHAR(255) NOT NULL
		-- FOREIGN KEY (Username) REFERENCES users(Username)
);

ALTER TABLE passwords
ADD FOREIGN KEY (Username) REFERENCES users(Username);

CREATE TABLE 
	permissions (
		Username VARCHAR(255),
		PermissionLevel VARCHAR(255) PRIMARY KEY
		-- FOREIGN KEY (Username) REFERENCES users(Username)
);

ALTER TABLE permissions
ADD FOREIGN KEY (Username) REFERENCES users(Username);

CREATE TABLE 
	threshold_limits (
		threshold_category VARCHAR(255) PRIMARY KEY,
		threshold_value INT NOT NULL,
		threshold_owner VARCHAR(255) NOT NULL,
		units VARCHAR(255) NOT NULL
);

ALTER TABLE permissions
ADD FOREIGN KEY (Username) REFERENCES users(Username);
	
