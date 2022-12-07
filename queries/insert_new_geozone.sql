INSERT INTO geozones (
    id,
    name
)
VALUES (
    md5(random()::text)::UUID,
    $1
)
ON CONFLICT (name) DO NOTHING;
