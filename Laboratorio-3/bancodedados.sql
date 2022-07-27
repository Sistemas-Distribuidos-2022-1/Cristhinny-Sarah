CREATE DATABASE "SistemasDistribuidos"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

CREATE TABLE ex1 (
	nome varchar(50) NOT NULL,
	cargo varchar(20) NOT NULL,
	salario integer NOT NULL
);

INSERT INTO ex1 (nome, cargo, salario) 
VALUES ('Joao','programador', 10000);

CREATE TABLE ex2 (
	nome varchar(50) NOT NULL,
	sexo varchar(20) NOT NULL,
	idade integer NOT NULL
);

INSERT INTO ex2 (nome, sexo, idade) 
VALUES ('Maria','feminino', 20);

CREATE TABLE ex3 (
	n1 numeric(10,1) NOT NULL,
	n2 numeric(10,1) NOT NULL,
	n3 numeric(10,1) NOT NULL
);

INSERT INTO ex3 (n1, n2, n3) 
VALUES (1.0, 6.0, 10.0);

CREATE TABLE ex4 (
	altura numeric(10,5) NOT NULL,
	sexo varchar(20) NOT NULL
);

INSERT INTO ex4 (altura, sexo) 
VALUES (2.15, 'masculino');

CREATE TABLE ex5 (
	idade integer NOT NULL
);

INSERT INTO ex5 (idade) 
VALUES (25);

CREATE TABLE ex6 (
	nome varchar(50) NOT NULL, 
	nivel varchar(1) NOT NULL, 
	salarioBruto numeric(10,2) NOT NULL, 
	numeroDeDependentes integer NOT NULL
);

INSERT INTO ex6 (nome, nivel, salarioBruto, numeroDeDependentes) 
VALUES ('Jaqueline', 'A', 10000, 25);

CREATE TABLE ex7 (
	idade integer NOT NULL, 
	tempoDeServico integer NOT NULL
);

INSERT INTO ex7 (idade, tempoDeServico) 
VALUES (50, 20);

CREATE TABLE ex8 ( 
	saldoMedio numeric(10,2) NOT NULL
);

INSERT INTO ex8 (saldoMedio) 
VALUES (15000);