INSERT INTO passengers (
    id,
    phone_number,
    password 
)
VALUES (
    md5(random()::text)::UUID,
    $1,
    $2
)
ON CONFLICT (phone_number) DO NOTHING
RETURNING id;
