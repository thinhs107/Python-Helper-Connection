import psycopg2
from psycopg2 import Error

from Helper.PostgreSQLConfig import *

cursor = ''


def conn_to_db(sql_statement, database, values):
    # insert_statement = """INSERT INTO config.Case(case_number) VALUES(%s) ;"""

    # insert_statement = sql_statement

    try:
        conn = psycopg2.connect(user=USER,
                                password=PASSWORD,
                                host="",
                                port=PORT,
                                database=database)
        cursor = conn.cursor()

        # print("PostgreSQL server information")
        # print(conn.get_dsn_parameters(), "\n")

        # cursor.execute('DELETE FROM config.Case')
        cursor.execute(sql_statement, values)

        conn.commit()
        # record = cursor.fetchone()
        # print("Number of records- ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (conn):
            cursor.close()
            conn.close()
            # print("PostgreSQl connection is closed")


def crypto_insert_into_db(json_input_value):
    return True




