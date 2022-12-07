import psycopg2
from psycopg2 import Error

from . import connections

def get_query() -> str:
    with open("queries/insert_new_user.sql", "r") as file:
        return file.read()


def insert_user(phone_number: str, password: str):
    try:
        try:
            connection = psycopg2.connect(connections.DSN)
            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            with connection.cursor() as cursor:
                query_pattern = get_query()
                query_pattern = query_pattern.replace("$1", phone_number)
                query_pattern = query_pattern.replace("$2", "'" + password + "'")
                cursor.execute(query_pattern)
        finally:
            if connection:
                connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


if __name__ == "__main__":
    insert_user("+78005553535", "admin")
