SELECT
    drivers.id,
    drivers.driver_name,
    cars.id,
    cars.government_number,
    car_models.brand,
    car_models.model_name,
    drivers.is_active,
    drivers.has_active_order
FROM drivers
LEFT JOIN cars ON
    drivers.carID = cars.id
LEFT JOIN car_models ON
    car_models.id = cars.modelID
WHERE drivers.id = $1;
