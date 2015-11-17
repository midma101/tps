from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
slot = Table('slot', post_meta,
    Column('server', String(length=140), primary_key=True, nullable=False),
    Column('database', String(length=140)),
    Column('username', String(length=140)),
    Column('ticket', String(length=140)),
)

entry = Table('entry', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('ticket_name', String(length=140)),
    Column('server', String(length=140)),
    Column('timestamp', DateTime),
    Column('dev', String(length=140)),
    Column('db', String(length=140)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['slot'].create()
    post_meta.tables['entry'].columns['db'].create()
    post_meta.tables['entry'].columns['dev'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['slot'].drop()
    post_meta.tables['entry'].columns['db'].drop()
    post_meta.tables['entry'].columns['dev'].drop()
