"""Configures MySQL Database.
    :Fields:
    - 'SQLALCHEMY_DATABASE_URI': Address of database
    - 'SQLALCHEMY_MIGRATE_REPO': Sets database migration repository
    - 'SQLALCHEMY_TRACK_MODIFICATIONS:': Suppresses warnings 
    - 'SECRET_KEY': Key that allows access to database
    
    :Database Login:
    - 'username': chat 
    - 'password': chat
    - 'name': chat
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://chat:chat@localhost/chat'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'chat'
