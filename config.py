import os

# For a production app, you should use a secret key set in the environment
# The recommended way to generate a 64char secret key is to run:
# python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

# When deploying, set in the environment to the PostgreSQL URL
#connection_string = "postgresql://postgres:postgres@localhost:5432/exercises"
connection_string = "postgresql://anand:YufzojdPjU1OZlWIsfS0alA46xPZwpIo@dpg-cr69j1l2ng1s7395sa90-a.oregon-postgres.render.com/exercises_jhtk"
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', connection_string)
# When you use Flask's default settings, the application looks for the instance folder to store files
# that should persist across different runs of the application, but are specific to the instance (like your SQLite database).
