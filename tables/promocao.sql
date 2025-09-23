CREATE TABLE promo(
id SERIAL PRIMARY KEY,
produto TEXT NOT NULL,
preco NUMERIC(10,2) NOT NULL,
preco_promocional NUMERIC(10,2) NOT NULL,
descricao TEXT,
categoria_id INTEGER,
image_url TEXT,
link_promo TEXT,
fonte_api varchar(45) not null,

CONSTRAINT categoria_fk FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);

CREATE TABLE categoria(
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL
);