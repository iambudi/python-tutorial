import sqlite3
from random import randint
from sqlite3.dbapi2 import Connection, Error
from typing import Any, List


def conn_factory(db_name: str = "") -> Connection:
    conn = sqlite3.connect(":memory:" if db_name == "" else db_name)
    # make fecth data accesible as list of dict not tuple
    conn.row_factory = sqlite3.Row
    print("Connection created")
    return conn


def migrate_and_seed(conn: Connection) -> None:
    cursor = conn.cursor()  # command context
    cursor.execute("CREATE TABLE IF NOT EXISTS user (id int, name text, age int)")
    for user in ["administrator", "it_dept", "acc_dept", "mkt_dept"]:
        values = (randint(100, 1000), user, randint(20, 30))
        cursor.execute(
            """
                INSERT INTO user(id, name, age) 
                VALUES(?, ?, ?)
            """,
            values,
        )
    conn.commit()
    cursor.close()
    print("Migration and seed done")


def find_all(conn: Connection) -> List[Any]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()  # cursor.fetchone()
    print("Data fetch done")
    cursor.close()
    return result


def show(data: List[Any]):
    if len(data) == 0:
        print("No data")
        return

    """
    # result by default is list[tuple] so the data can be accessed by its col index
    # which is not informative. row[0] for id, row[2] for name so on.
    # to access by col name then the result must be as list[dict]
    """
    print("=" * 30)
    print("\t".join(data[0].keys()))  # print header from dict keys
    print("=" * 30)
    for row in data:
        print(f"{row['id']}\t{row['name']}\t{row['age']}")


# Test
try:
    conn = conn_factory()
    migrate_and_seed(conn)
    show(find_all(conn))
    conn.close()
except Error as error:
    print("parameterized query failed {}".format(error))
