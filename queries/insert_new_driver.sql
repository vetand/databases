INSERT INTO drivers (
    id,
    is_active,
    carID,
    agility_class,
    license,
    licence_expiration,
    rating,
    birth_of_date,
    driver_name
)
VALUES (
    md5(random()::text)::UUID,
    FALSE,
    $1,
    5,
    $2,
    '2040-09-27',
    5.0,
    '1980-09-27',
    $3
)
RETURNING id;
