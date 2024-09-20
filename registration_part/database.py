import psycopg2
from main import name,age,gender
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
    cur.execute(""" INSERT INTO person (name, age, gender) VALUES
                ('John', 25, 'M'),
                ('Jane', 30, 'F'),
                ('Bob', 40, 'M'),
                ('Engeline', 19, 'F');
                """)

    conn.commit()
#input Data
def input_data(age,name,gender):
    #insert data
    if name and age and gender not in :
    cur.execute(f""" INSERT INTO person (name, age, gender) VALUES({age},{name},{gender});""")
    conn.commit

#Select data
def select_Data():
    cur.execute(""" SELECT * from person""")
    return cur.fetchall()
cur.close
conn.close()