import psycopg2
import os
from psycopg2 import Error

import connections

MIGRATIONS_DIR_PATH = "migrations"


def get_migrations() -> [str]:
    all_files = []
    for (dirpath, dirnames, filenames) in os.walk(MIGRATIONS_DIR_PATH):
        all_files.extend(filenames)
        break

    result = []
    for file in all_files:
        filename, file_extension = os.path.splitext(MIGRATIONS_DIR_PATH + "/" + file)
        if file_extension == ".sql":
            result.append(str(MIGRATIONS_DIR_PATH + "/" + file))
    result.sort()
    return result


if __name__ == "__main__":
    try:
        for migration_file in get_migrations():
            with open(migration_file, "r") as file:
                migration_query = file.read()

            print("===================================================================")
            print(migration_file)
            print("===================================================================")
            print(migration_query)
            print("===================================================================")
            print()
            print()

            try:
                connection = psycopg2.connect(connections.DSN)
                connection.set_isolation_level(
                    psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
                )
                with connection.cursor() as cursor:
                    cursor.execute(migration_query)
            finally:
                if connection:
                    connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
