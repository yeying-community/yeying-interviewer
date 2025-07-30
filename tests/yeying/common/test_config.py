import logging
import os

from interviewer.domain.mapper.entities import DbModel
from interviewer.infrastructure.db.instance import DatabaseConfig, ensure_migrated


def setup_test_database(tables: list[DbModel]) -> DatabaseConfig:
    file_path = "/tmp/test.sqlite"
    if os.path.exists(file_path):
        os.remove(file_path)
    config = DatabaseConfig(type="sqlite", name=file_path)
    ensure_migrated(config=config, tables=tables)
    return config


def setup_test_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()],
    )
