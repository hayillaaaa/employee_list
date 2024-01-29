CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employees (
    id int primary key auto_increment,
    last_name varchar(255),
    first_name varchar(255),
    address varchar(255),
    city varchar(64),
    country varchar(64),
    birthdate date,
    created_on datetime DEFAULT CURRENT_TIMESTAMP,
    updated_on datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    department_id int
);

CREATE TABLE department (
    id int primary key auto_increment,
    name varchar(255),
    created_on datetime DEFAULT CURRENT_TIMESTAMP,
    updated_on datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
);



