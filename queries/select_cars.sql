SELECT
    cars.government_number,
    car_models.brand,
    car_models.model_name
FROM cars
LEFT JOIN car_models ON
    car_models.id = cars.modelID
LIMIT $1;
