SELECT
    geozones.name,
    geozone_coordinates.longitude,
    geozone_coordinates.latitude
FROM geozone_coordinates
LEFT JOIN geozones ON
    geozone_coordinates.zoneID = geozones.id
WHERE geozones.name = $1;
