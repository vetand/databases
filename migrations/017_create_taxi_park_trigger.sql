CREATE OR REPLACE FUNCTION do_create_taxi_park() RETURNS TRIGGER AS $taxi_parks$
   BEGIN
      INSERT INTO taxi_parks(
          id,
          zoneID
      ) VALUES (
          md5(random()::text)::UUID,
          new.id
      );
      RETURN new;
   END;
$taxi_parks$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS create_taxi_park on geozones;

CREATE TRIGGER create_taxi_park AFTER INSERT ON geozones
FOR EACH ROW EXECUTE PROCEDURE do_create_taxi_park();
