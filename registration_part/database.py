from config_database import username,password,host,port,dbname
conn_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
