CREATE TABLE IF NOT EXISTS geozones (
    id UUID NOT NULL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
