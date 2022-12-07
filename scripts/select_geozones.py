import psycopg2
from psycopg2 import Error

from . import connections

def get_query_one() -> str:
    with open("queries/select_geozone.sql", "r") as file:
        return file.read()


def get_query_many() -> str:
    with open("queries/select_geozones.sql", "r") as file:
        return file.read()


def fetch_by_name(name: str) -> dict:
    try:
        connection = psycopg2.connect(connections.DSN)
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        with connection.cursor() as cursor:
            query_pattern = get_query_one()
            query_pattern = query_pattern.replace("$1", "'" + name + "'")
            cursor.execute(query_pattern)
            result = cursor.fetchone()
            return {"id": result[0], "name": result[1]}
    finally:
        if connection:
            connection.close()


def select_geozones(limit: int):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query_many()
                query_pattern = query_pattern.replace("$1", str(limit))
                cursor.execute(query_pattern)
                print(cursor.fetchall())
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


if __name__ == "__main__":
    select_geozones(10)
