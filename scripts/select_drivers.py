import psycopg2
from psycopg2 import Error

from . import connections

def get_query() -> str:
    with open("queries/select_drivers.sql", "r") as file:
        return file.read()

def get_query_active() -> str:
    with open("queries/select_active_drivers.sql", "r") as file:
        return file.read()

def get_query_one() -> str:
    with open("queries/select_driver.sql", "r") as file:
        return file.read()

def select_driver(driver_id: str):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query_one()
                query_pattern = query_pattern.replace("$1", "'" + driver_id + "'")
                cursor.execute(query_pattern)
                return cursor.fetchone()
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

def select_drivers(limit: int):
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
                return cursor.fetchall()
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

def select_active_drivers(limit: int):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query_active()
                query_pattern = query_pattern.replace("$1", str(limit))
                cursor.execute(query_pattern)
                return cursor.fetchall()
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

if __name__ == "__main__":
    select_drivers(10)
