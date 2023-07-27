from environs import Env
from dotenv import load_dotenv


load_dotenv()
env = Env()


class Settings:
    API_HOST = env.str("API_HOST")
    LOGIN = env.str("LOGIN")
    PASSWORD = env.str("PASSWORD")
