DROP DATABASE IF EXISTS project_management;

CREATE DATABASE project_management;

CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cost MONEY NOT NULL,
    company_id SERIAL REFERENCES company (id)
);
