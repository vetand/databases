CREATE TABLE IF NOT EXISTS passengers (
    id UUID NOT NULL PRIMARY KEY,
    phone_number TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL  
);
