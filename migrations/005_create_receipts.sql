CREATE TABLE IF NOT EXISTS receipts (
    id UUID NOT NULL PRIMARY KEY,
    price float NOT NULL,
    receiptURL TEXT
);
