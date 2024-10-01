from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy import Integer,Text,Column,insert,values
engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/sqlalchemy_tuts", 
    echo=False)
conn = engine.connect()
metadata = MetaData()
books = Table("name",metadata,
              Column("age",Integer),
              Column("Name",Text,primary_key=True),
              Column("IP",Text)
)
metadata.create_all(engine)
ins = books.insert().values([
    {'age':18,'Name':'Daniil','IP':'127.0.0.1:8000'}
])
conn.execute(ins)
conn.commit()
