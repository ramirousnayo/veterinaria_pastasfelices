# config/settings/__init__.py
import os
from dotenv import load_dotenv

load_dotenv()

DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

if DJANGO_ENV == 'production':
    from .production import *
else:
    from .development import *