import psycopg2
from psycopg2 import Error

from . import connections

def get_query() -> str:
    with open("queries/insert_new_order.sql", "r") as file:
        return file.read()

def create_taxi_order(a_longitude, a_latidude, b_longitude, b_latitude, price, driver_id):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query()
                query_pattern = query_pattern.replace("$1", str(a_longitude))
                query_pattern = query_pattern.replace("$2", str(b_latitude))
                query_pattern = query_pattern.replace("$3", str(a_longitude))
                query_pattern = query_pattern.replace("$4", str(b_latitude))
                query_pattern = query_pattern.replace("$5", "'" + driver_id + "'")
                query_pattern = query_pattern.replace("$6", str(price))
                cursor.execute(query_pattern)
                order = cursor.fetchone()
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

if __name__ == "__main__":
    create_taxi_order(55.0, 37.0, 56.0, 38.0, '500', None)
