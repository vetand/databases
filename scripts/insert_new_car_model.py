import psycopg2
from psycopg2 import Error

from . import connections

def get_query() -> str:
    with open("queries/insert_new_car_model.sql", "r") as file:
        return file.read()


def insert_car_model(brand: str, model: str, description: str):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query()
                query_pattern = query_pattern.replace("$1", "'" + brand + "'")
                query_pattern = query_pattern.replace("$2", "'" + model + "'")
                query_pattern = query_pattern.replace("$3", "'" + description + "'")
                cursor.execute(query_pattern)

                return cursor.fetchone()
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


if __name__ == "__main__":
    insert_car_model("BMW", "X5", "Розовенькая бэшка (^-^)")
