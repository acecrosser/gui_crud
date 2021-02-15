import mysql.connector as mysql
from mysql.connector import errorcode

config = {
    'user': 'gui_admin',
    'password': '',
    'host': '127.0.0.1',
    'database': 'db_gui_crud',
    'raise_on_warnings': True,
}

DB_NAME = 'db_gui_crud'

TABLES = {}
TABLES['wish_list'] = (
    "CREATE TABLE `wish_list` ("
    " `id` smallint NOT NULL AUTO_INCREMENT,"
    " `title` varchar(150) NOT NULL,"
    " `price` float,"
    " `link` text,"
    " `about` text,"
    " `done` boolean default false,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

connect = mysql.connect(**config)


if __name__ == '__main__':

    def create_database():
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'UTF8MB4'".format(DB_NAME))
        except mysql.Error as err:
            print(f'Failed creating database: {err}')
            exit(1)


    config_2 = {
        'user': 'gui_admin',
        'password': '',
        'host': '127.0.0.1',
        'raise_on_warnings': True,
    }

    connect = mysql.connect(**config_2)
    cursor = connect.cursor()

    try:
        cursor.execute(f'USE {DB_NAME}')
    except mysql.Error as err:
        print(f'Database {DB_NAME} does not exists.')
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database()
            print(f'Database {DB_NAME} created successfully.')
            connect.database = DB_NAME
        else:
            print(err)
            exit(1)

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print(f'Create table {table_name}: ', end='')
            cursor.execute(table_description)
        except mysql.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Table exists.')
            else:
                print(err.msg)
        else:
            print('OK')

    cursor.close()
    connect.close()

