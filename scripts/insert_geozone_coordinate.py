import psycopg2
from psycopg2 import Error

from . import connections
from . import select_geozones

def get_query_select() -> str:
    with open("queries/select_geozone.sql", "r") as file:
        return file.read()


def get_query_insert() -> str:
    with open("queries/insert_new_geozone_coordinate.sql", "r") as file:
        return file.read()


def insert_geozone_coordinate(zone_name: str, longitude: float, latitude: float):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                zone_id = select_geozones.fetch_by_name(zone_name)["id"]

                query_pattern = get_query_insert()
                query_pattern = query_pattern.replace("$1", "'" + zone_id + "'")
                query_pattern = query_pattern.replace("$2", str(longitude))
                query_pattern = query_pattern.replace("$3", str(latitude))
                cursor.execute(query_pattern)
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


if __name__ == "__main__":
    insert_geozone_coordinate("moscow", 55.0, 36.0)
    insert_geozone_coordinate("moscow", 56.0, 36.0)
    insert_geozone_coordinate("moscow", 56.0, 37.0)
    insert_geozone_coordinate("moscow", 55.0, 37.0)
