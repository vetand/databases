CREATE TABLE IF NOT EXISTS drivers (
    id UUID NOT NULL PRIMARY KEY,
    is_active boolean NOT NULL,
    carID UUID NOT NULL UNIQUE,
    agility_class int,
    license TEXT NOT NULL UNIQUE,
    licence_expiration DATE,
    rating float,
    birth_of_date DATE
);
