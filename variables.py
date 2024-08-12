import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv('ENV')
BYTE_SCORES_PATH = os.getenv('BYTE_SCORES_PATH')
LOGS_PATH = os.getenv('LOGS_PATH')
TEXT_SCORES_PATH = os.getenv('TEXT_SCORES_PATH')