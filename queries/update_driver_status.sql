BEGIN;


UPDATE active_orders
SET finished_ts = NOW()
FROM drivers
WHERE drivers.id = $3 AND drivers.id = $3;

UPDATE drivers
SET is_active = $1, has_active_order = $2
WHERE drivers.id = $3;

COMMIT;
