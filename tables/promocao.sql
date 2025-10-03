CREATE DATABASE IF NOT EXISTS "ETL_Products";
\c "ETL_Products";

CREATE TABLE IF NOT EXISTS categoria(
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS produto(
id serial primary key,
codigo integer not null unique,
nome_produto TEXT NOT NULL unique,
descricao TEXT,
preco_base numeric(10,2) not null,
preco_promocional numeric(10,2),
id_categoria integer,
CONSTRAINT id_categoria FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);

CREATE TABLE IF NOT EXISTS classificacao(
id serial primary key,
produto_id integer UNIQUE,
quantidade_classificacao integer not null,
nota_media numeric(10,2) not null,
CONSTRAINT produto_id FOREIGN KEY (produto_id) REFERENCES produto(id)
);

CREATE TABLE IF NOT EXISTS promocao(
id SERIAL PRIMARY KEY,
produto_id INTEGER UNIQUE,
tipo_promocao varchar(45) not null,
fonte_api varchar(45) not null,
CONSTRAINT produto_id FOREIGN KEY (produto_id) REFERENCES produto(id)
);





