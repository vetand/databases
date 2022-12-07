CREATE TABLE IF NOT EXISTS feedbacks (
    id UUID NOT NULL PRIMARY KEY,
    userID UUID NOT NULL,
    driverID UUID NOT NULL,
    feedback int,
    created_ts TIMESTAMP NOT NULL
);
