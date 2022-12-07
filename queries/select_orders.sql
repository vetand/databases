SELECT
    active_orders.id,
    active_orders.price,
    active_orders.userID,
    active_orders.driverID,
    active_orders.created_ts,
    active_orders.finished_ts
FROM active_orders
ORDER BY created_ts DESC
LIMIT $1;
