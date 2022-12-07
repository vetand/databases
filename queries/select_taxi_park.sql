SELECT
    taxi_parks.id,
    geozones.name
FROM taxi_parks
LEFT JOIN geozones ON
    geozones.id = taxi_parks.zoneID
WHERE geozones.name = $1;
