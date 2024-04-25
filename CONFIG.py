import os
from dotenv import load_dotenv


load_dotenv()


ENVIRONMENT = os.getenv("ENVIRONMENT")

DATABASE_URL = os.getenv(f"{ENVIRONMENT}_DATABASE_URL")
DATABASE_CONNECT_ARGS = {"check_same_thread": False} if ENVIRONMENT=="DEVELOPMENT" else None
