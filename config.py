from server import app, logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import QueuePool
import psycopg2

logging.info('In config.py')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/lang'
app.config['SQLALCHEMY_BINDS'] = {'lang': 'sqlite:///langs.db', 'LANG': 'postgresql://postgres:root@localhost:5432/lang', 'dblang': 'mysql://root:root@localhost/tests'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# a QueuePool integrated, pre-configured with reasonable pooling defaults.
# QueuePool(creator, pool_size=5, max_overflow=10, timeout=30, use_lifo=False, **kw
# Disabling pooling using NullPool: {"poolclass": NullPool}

engine1 = db.create_engine('sqlite:///langs.db', {"poolclass": QueuePool, "pool_use_lifo": True})
engine2 = db.create_engine('postgresql+psycopg2://postgres:root@localhost:5432/lang', {"pool_size": 10, "max_overflow": 20, "pool_pre_ping": True})
engine3 = db.create_engine('mysql+mysqldb://root:root@localhost/test', {'echo': True, 'pool_size': 5, 'max_overflow': 15,'pool_recycle': 3600})


logging.info('Database configured')