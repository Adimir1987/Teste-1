-- ==========================================
-- TABELA: endereco
-- ==========================================
CREATE TABLE endereco (
    id_endereco SERIAL PRIMARY KEY,
    referencia VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT
);
