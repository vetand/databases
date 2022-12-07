INSERT INTO geozone_coordinates (
    id,
    zoneID,
    longitude,
    latitude
)
VALUES (
    md5(random()::text)::UUID,
    $1,
    $2,
    $3
);
