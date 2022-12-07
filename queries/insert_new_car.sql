INSERT INTO cars (
    id,
    modelID,
    parkID,
    government_number
)
VALUES (
    md5(random()::text)::UUID,
    $1,
    md5(random()::text)::UUID,
    $2
)
RETURNING id;
