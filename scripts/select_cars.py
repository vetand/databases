import psycopg2
from psycopg2 import Error

from . import connections

def get_query() -> str:
    with open("queries/select_cars.sql", "r") as file:
        return file.read()


def select_cars(limit: int):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query()
                query_pattern = query_pattern.replace("$1", str(limit))
                cursor.execute(query_pattern)
                print(cursor.fetchall())
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


if __name__ == "__main__":
    select_cars(10)
