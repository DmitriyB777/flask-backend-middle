class Config(object):
    username = 'postgres'
    password = 'root'
    host = '127.0.0.1'
    port = 5432
    database = 'flask-backend-middle-db'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{host}:{port}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False