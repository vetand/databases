import psycopg2
from psycopg2 import Error

from . import connections

def get_query() -> str:
    with open("queries/update_driver_status.sql", "r") as file:
        return file.read()

def update_driver_status(status: str, has_order: str, driver_id: str):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query()
                query_pattern = query_pattern.replace("$1", status)
                query_pattern = query_pattern.replace("$2", has_order)
                query_pattern = query_pattern.replace("$3", "'" + driver_id + "'")

                cursor.execute(query_pattern)
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

if __name__ == "__main__":
    pass
