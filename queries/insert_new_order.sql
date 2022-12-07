UPDATE drivers SET
is_active = FALSE,
has_active_order = TRUE
WHERE drivers.id = $5;

INSERT INTO active_orders (
    id,
    pointAlongitude,
    pointAlatitude,
    pointBlatitude,
    pointBlongitude,
    userID,
    driverID,
    tariffID,
    price,
    created_ts,
    finished_ts
)
VALUES (
    md5(random()::text)::UUID,
    $1,
    $2,
    $3,
    $4,
    md5(random()::text)::UUID,
    $5,
    md5(random()::text)::UUID,
    $6,
    NOW(),
    NULL
)
RETURNING id;
