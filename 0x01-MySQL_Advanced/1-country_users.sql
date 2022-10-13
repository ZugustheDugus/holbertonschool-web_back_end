-- create user tables with these requirements
-- 1. id is a primary key never null auto increment auto increment
-- 2. email string never null and unique
-- 3. name string
-- 4. country string never null enumberation of countries US, CO, TN

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL,
	PRIMARY KEY (id)
);