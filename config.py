import os
from dotenv import load_dotenv 

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

API_TOKEN = os.environ.get('API_TOKEN')
INSTANCE_ID= os.environ.get('INSTANCE_ID')
SECRET_KEY = os.urandom(32)

