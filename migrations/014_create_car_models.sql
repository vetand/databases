CREATE TABLE IF NOT EXISTS car_models (
    id UUID NOT NULL PRIMARY KEY,
    brand TEXT NOT NULL,
    model_name TEXT NULL,
    description TEXT,
    UNIQUE(brand, model_name)
);
