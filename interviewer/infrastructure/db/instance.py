import logging
from contextlib import contextmanager

from peewee import SqliteDatabase, PostgresqlDatabase, MySQLDatabase, OperationalError
from playhouse.migrate import SqliteMigrator, PostgresqlMigrator, MySQLMigrator, migrate, SchemaMigrator
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from interviewer.domain.mapper.entities import database_proxy, SchemaMigration, DbModel
from interviewer.tool.file import ensure_parent_dirs_exist

migrator: SchemaMigrator = None

CURRENT_VERSION = "2025-02-18"


class DatabaseConfig(BaseModel):
    type: str = "sqlite"
    host: str = "localhost"
    port: int = 5432
    user: str = None
    password: str = None
    name: str = "metadata/sqlite3.db"


def create_database(config: DatabaseConfig):
    global migrator
    """
    Create a database object based on the given configuration.

    :param config: A dictionary containing the database configuration.
    :return: A Peewee database object.
    """
    if config.type == 'sqlite':
        database = SqliteDatabase(ensure_parent_dirs_exist(config.name))
        database_proxy.initialize(database)
        migrator = SqliteMigrator(database)
    elif config.type == 'postgresql':
        database = PostgresqlDatabase(
            config.name,
            user=config.user,
            password=config.password,
            host=config.host,
            port=config.port,
        )

        database_proxy.initialize(database)
        migrator = PostgresqlMigrator(database)

    elif config.type == 'mysql':
        database = MySQLDatabase(
            config.name,
            user=config.user,
            password=config.password,
            host=config.host,
            port=config.port,
        )
        database_proxy.initialize(database)
        migrator = MySQLMigrator(database)
    else:
        raise ValueError(f"Unsupported database type: {config.type}")


def alter(schema: SchemaMigration, ops: list[list], version: str) -> bool:
    try:
        migrate(*ops)
    except OperationalError as e:
        print("Migration failed", e)
        return False
    schema.version = version
    schema.save()
    print(f"Migrated {version}")
    return version != CURRENT_VERSION


def perform_migration(schema: SchemaMigration) -> bool:
    pass


def ensure_migrated(config: DatabaseConfig, tables: list[DbModel]):
    create_database(config)

    if not database_proxy.table_exists(SchemaMigration):
        tables.append(SchemaMigration)
        database_proxy.create_tables(tables)
        SchemaMigration.create(version=CURRENT_VERSION)

    schema = SchemaMigration.select().first()
    if schema.version != CURRENT_VERSION:
        perform_migration(schema)


class Instance(object):
    """Connect to postgresql database and execute crud command,
    reference: https://docs.sqlalchemy.org/en/14/orm/examples.html
    """

    def __init__(self, conf=None):
        address = 'postgresql://{}:{}@{}:{}/{}'.format(conf.user, conf.password, conf.host, conf.port, conf.name)
        self.engine = create_engine(address)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        logging.info('Success to connect to interviewer database={}:{}!'.format(conf.host, conf.port))

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = sessionmaker(bind=self.engine)()
        try:
            yield session
            session.commit()
        except Exception as e:
            logging.error(f'Fail to yield session to interviewer database, error=${str(e)}!', exc_info=True)
            session.rollback()
            raise e
        finally:
            session.close()

    def get_session(self):
        return self.session

    def insert(self, records):
        with self.session_scope() as session:
            if not isinstance(records, list):
                session.add(records)
                return

            for record in records:
                session.add(record)

    def close(self):
        if self.session is None:
            return
        self.session.close()