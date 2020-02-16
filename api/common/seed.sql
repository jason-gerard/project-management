\connect postgres

DROP DATABASE IF EXISTS project_management;

CREATE DATABASE project_management;

\connect project_management

CREATE TABLE company (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE project (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cost MONEY NOT NULL,
    company_id INT NOT NULL REFERENCES company (id),
    parent_project_id INT REFERENCES project (id)
);
