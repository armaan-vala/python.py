#sql: structured query Language
#pip install




db-sqlite3 import sqlite3
def connect(dbname):
conn = sqlite3.connect(dbname)


conn.execute("CREATE TABLE IF NOT EXISTS OYO HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")


print("Table created successfully!")

conn.close()

def insert_into_table(dbname, values):

 conn = sqlite3.connect(dbname)


print("Inserted into table: " + str(values))
insert_sql "INSERT INTO OYO HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?, ?, ?, ?, ?)" =

conn.execute(insert_sql, values)

conn.commit()
conn.close()

def get_hotel_info(dbname):
conn = sqlite3.connect(dbname)