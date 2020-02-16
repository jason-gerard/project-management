\connect postgres

DROP DATABASE IF EXISTS project_management;

CREATE DATABASE project_management;

\connect project_management

CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255 ) NOT NULL
);

CREATE TABLE project (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cost MONEY NOT NULL,
    company_id INT NOT NULL REFERENCES company (id) ON DELETE CASCADE,
    parent_project_id INT REFERENCES project (id) ON DELETE CASCADE
);
