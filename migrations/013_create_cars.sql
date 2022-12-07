CREATE TABLE IF NOT EXISTS cars (
    id UUID NOT NULL PRIMARY KEY,
    modelID UUID NOT NULL,
    parkID UUID NOT NULL,
    government_number TEXT NOT NULL
);
