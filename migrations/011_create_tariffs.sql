CREATE TABLE IF NOT EXISTS tariffs (
    id UUID NOT NULL PRIMARY KEY,
    price_coef float NOT NULL,
    agility_class int
);
