from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
DB = Table('DB', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
)

dev = Table('dev', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
)

entry = Table('entry', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('ticket_name', String(length=140)),
    Column('server', String(length=140)),
    Column('timestamp', DateTime),
    Column('username', String(length=140)),
    Column('database', String(length=140)),
)

server = Table('server', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
)

ticket = Table('ticket', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['DB'].create()
    post_meta.tables['dev'].create()
    post_meta.tables['entry'].create()
    post_meta.tables['server'].create()
    post_meta.tables['ticket'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['DB'].drop()
    post_meta.tables['dev'].drop()
    post_meta.tables['entry'].drop()
    post_meta.tables['server'].drop()
    post_meta.tables['ticket'].drop()
