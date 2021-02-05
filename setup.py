import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'fairedb'

TABLES = {}

TABLES['spoted_brand'] = (
    "CREATE TABLE `spoted_brand` ("
    "`id` int(100) NOT NULL,"
    "`name` varchar(250),"
    "`country` varchar(250),"
    "`date` date,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

def create_table():
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({}) ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Alerady Exists")
            else:
                print(err.msg)

create_database()
create_table()