-- create table users with these requirements
-- 1. id is a primary key never null auto increment
-- 2. email string never null and unique
-- 3. name string 

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id)
);