CREATE TABLE IF NOT EXISTS geozone_coordinates (
    id UUID NOT NULL PRIMARY KEY,
    zoneID UUID NOT NULL,
    longitude float NOT NULL,
    latitude float NOT NULL,
    UNIQUE (zoneID, longitude, latitude)
);
