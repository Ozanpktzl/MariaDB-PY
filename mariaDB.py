import mysql.connector as mariadb

mariadb_connector = mariadb.connect(
    user="username",
    password="password",
    database="test",
    host="localhost",
    port="3306"
)
create_cursor = mariadb_connector.cursor()
create_cursor.execute("CREATE DATABASE test_database")
create_cursor.execute("SHOW DATABASES")
for x in create_cursor:
    print(x)