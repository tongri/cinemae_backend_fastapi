from decouple import config

db_user = config("db_user")
db_password = config("password")
db_host = config("host")
db_port = config("port")
db_name = config("db_name")

ASYNC_DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
database = "databases.Database(DATABASE_URL)"
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
