INSERT INTO car_models (
    id,
    brand,
    model_name,
    description
)
VALUES (
    md5(random()::text)::UUID,
    $1,
    $2,
    $3
)
ON CONFLICT (brand, model_name) DO UPDATE
SET description = $3
RETURNING id;
