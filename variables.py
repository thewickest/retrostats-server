import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv('ENV')
BYTE_SCORES_PATH = os.getenv('BYTE_SCORES_PATH')
LOGS_PATH = os.getenv('LOGS_PATH')
TEXT_SCORES_PATH = os.getenv('TEXT_SCORES_PATH')
API_URL = os.getenv('API_URL')
API_USER = os.getenv('API_USER')
API_PASSWORD = os.getenv('API_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')