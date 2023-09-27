import psycopg2

dataBase = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="batur",
    host="localhost",
    port="5432"
)

cursorObject = dataBase.cursor()
dataBase.autocommit = True

cursorObject.execute("CREATE DATABASE MyCompany;")