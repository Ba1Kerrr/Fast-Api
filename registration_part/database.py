import psycopg2
# Подключение к базе данных
conn = psycopg2.connect(
    dbname='sqlalchemy_tuts',
    user='postgres',
    password='root',
    host='localhost',  # или другой адрес вашего сервера
    port='5432'        # стандартный порт PostgreSQL
)
cursor = conn.cursor()

# Создание таблицы, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS site_registrations (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
''')

def find_users(email):
    a = []
    for i in range(2):
        cursor.execute(
        '''
        SELECT %s,COUNT(*)
        FROM site_registrations
        GROUP BY %s
        HAVING COUNT(*) > 1;'''
        ,email)
        a.append(cursor.fetchall() [2:-3])
    return int( str( cursor.fetchall() ) [2:-3])

def insert_values(full_name, username, email, password):
    # Вставка значений в таблицу
    cursor.execute('''
        INSERT INTO site_registrations (full_name, username, email, password)
        VALUES (%s, %s, %s, %s)''',
        (full_name, username, email, password))

    # Сохранение изменений и закрытие соединения
    conn.commit()