import sqlite3
from sqlite3 import Error


def create_connection(db_file: str):
    '''Create the connection for the database.
    returns instance of class connection or None'''

    conn = None

    try:
        print(db_file)
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn: str, create_table_sql: str):
    '''create the table with conn instance with create_table_sql statement.
    '''

    try:
        c = conn.cursor() 
        '''cursor object allows to send the sql command to execute.'''
        c.execute(create_table_sql)
        '''execute command - method which is responsible for sending the command.'''
    except Error as e:
        print(e)

def create_project(conn, login,  password):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    values = f'VALUES({login},{password})'
    sql = ''' INSERT INTO users(login,password) VALUES(?,?)'''
    '''sql command line to insert values into fields in table users.
    NOT NULL params are required to be filled. Other params are optional.'''
    cur = conn.cursor()
    cur.execute(sql,('user2','1234'))
    '''execute(command, iterable)
    if you want to insert values into table, use sql command 
    INSERT INTO  #table name#(*args)
    cur.execute(sql_command, values: iterable) len(values) == len(*args)'''
    conn.commit()
    return cur.lastrowid

def print_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"/Users/nikitadereza/PycharmProjects/Study/login.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        login text NOT NULL,
                                        password text NOT NULL 
                                    ); """
    '''Sql code to create table if table users does not exist, table name can be changed.
    Table parameteres also can be changed. login and password parameters text objects.
    if field must be filled in - set NOT NULL next to param.'''


    # create a database connection
    conn = create_connection(database)


    # create tables
    if conn is not None:
        print_data(conn)
        # create_project(conn, login='', password='')
        # create projects table
        # create_table(conn, sql_create_projects_table)
        

    else:
        print("Error! cannot create the database connection.")
main()