CREATE TABLE local (
    id_local SERIAL PRIMARY KEY,
    idendereco INT NOT NULL,
    nome VARCHAR(100) NOT NULL,

    CONSTRAINT fk_local_endereco
        FOREIGN KEY (idendereco)
        REFERENCES endereco(id_endereco)
);