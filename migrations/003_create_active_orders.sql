CREATE TABLE IF NOT EXISTS active_orders (
    id UUID NOT NULL PRIMARY KEY,
    pointAlongitude float NOT NULL,
    pointAlatitude float NOT NULL,
    pointBlatitude float NOT NULL,
    pointBlongitude float NOT NULL,
    userID UUID NOT NULL,
    driverID UUID,
    tariffID UUID NOT NULL,
    price float,
    created_ts TIMESTAMP,
    finished_ts TIMESTAMP
);
