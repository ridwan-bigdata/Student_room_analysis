CREATE DATABASE students_rooms;

USE students_rooms;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS rooms;
CREATE TABLE rooms (
id INT PRIMARY KEY,
name VARCHAR(50)
);

CREATE TABLE students (
id INT PRIMARY KEY,
name VARCHAR (100),
room INT,
sex CHAR (1),
birthday DATETIME, 
FOREIGN KEY (room) REFERENCES rooms(id)
);
