import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_chromosome(conn, chromosome):
    """
    Create a new task
    :param conn:
    :param chromosome:
    :return:
    """

    sql = ''' INSERT INTO data(generation,fitness,chromosome)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, chromosome)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"database.db"

    sql_create_data_table = """ CREATE TABLE IF NOT EXISTS data (
                                        id integer PRIMARY KEY,
                                        generation integer NOT NULL,
                                        fitness DOUBLE,
                                        chromosome text
                                    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_data_table)

        # create tasks table
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

    with conn:

        # Create a fake chromosome
        # Generation / Fitness / chromosome
        data1 = (0, 99, '[gene,gene,gene,gene]')
        data2 = (1, 200, '[gene,gene,gene,gene]')
        # Add chromosome to the data table inside the database
        create_chromosome(conn, data1)
        create_chromosome(conn, data2)


if __name__ == '__main__':
    main()
