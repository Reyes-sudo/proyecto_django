import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SQLITE={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

MYSQL = {
  'default':{
  'ENGINE':'django.db.backends.mysql',
  'NAME':os.environ.get('DBNAME'),
  'USER':os.environ.get('DBUSER'),
  'PASSWORD':os.environ.get('DBPASS'),
  'HOST':os.environ.get('DBHOST'),
  'PORT':'3306'
  }
}
