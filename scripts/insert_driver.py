import random
import psycopg2
from psycopg2 import Error

from . import connections
from . import select_geozones

def get_query_car() -> str:
    with open("queries/insert_new_car.sql", "r") as file:
        return file.read()

def get_query_driver() -> str:
    with open("queries/insert_new_driver.sql", "r") as file:
        return file.read()

def insert_new_driver(car_model: str, driver_name: str, gov_number: str):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query_car()
                query_pattern = query_pattern.replace("$1", "'" + car_model + "'")
                query_pattern = query_pattern.replace("$2", "'" + gov_number + "'")
                cursor.execute(query_pattern)
                result = cursor.fetchone()
                car_id = result[0]

                query_pattern = get_query_driver()
                query_pattern = query_pattern.replace("$1", "'" + car_id + "'")
                query_pattern = query_pattern.replace(
                    "$2", "'" + str(random.randrange(1000, 10000)) + "'"
                )
                query_pattern = query_pattern.replace("$3", "'" + driver_name + "'")
                cursor.execute(query_pattern)

                result = cursor.fetchone()
                return result[0]
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


if __name__ == "__main__":
    insert_new_driver("4d78d294-36f2-10a6-7f03-246ec8073a2c", "Аилбибек", "B77ОР77")
