import psycopg2
from main import name,age,email
conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "root",
    port = "5432"
)

cur = conn.cursor()
# New Data_base
def create_new_dastabase():
    cur.execute(""" INSERT INTO person (name, age, email) VALUES
                ('John', 25, 'M'),
                ('Jane', 30, 'F'),
                ('Bob', 40, 'M'),
                ('Engeline', 19, 'F');
                """)
#input Data
def input_data(age,name,email):
    #insert data
    if name and age and email != 0:
        cur.execute(f""" INSERT INTO person (name, age, email) VALUES({age},{name},{email});""")
        conn.commit()

#Select data
def select_Data():
    cur.execute(""" SELECT * from person""")
    return cur.fetchall()
cur.close
conn.close()