import logging
import os
from dataclasses import dataclass
from logging.handlers import RotatingFileHandler

import toml

from interviewer.infrastructure.db.instance import DatabaseConfig


@dataclass
class OpenaiConf:
    organization: str = None
    apiKey: str = None


@dataclass
class ServerConf:
    port: int = 9401
    cacheDir: str = '.cache'


@dataclass
class CredentialConf:
    certDir: str = None
    enable: bool = True


@dataclass
class LogConf:
    filename: str = None
    level: str = None
    format: str = None
    maxBytes: int = 536870912
    backupCount: int = 10


class Config(object):

    def __init__(self, filepath):
        logging.info(f'Use the configs={filepath}.')
        self.cfg = toml.load(filepath)

    def update_cert_dir(self, cert_dir):
        self.cfg['credential']['certDir'] = cert_dir

    def update_port(self, port):
        self.cfg['server']['port'] = port

    def update_cache_dir(self, cert_dir):
        self.cfg['server']['cacheDir'] = cert_dir

    def get_log(self):
        log = self.cfg.get('log', {}) if self.cfg is not None else None
        return LogConf(
            Config.get_value(log, 'filename', 'log/interviewer.log'),  # log/interviewer.log
            Config.get_value(log, 'level', 'INFO'),
            Config.get_value(log, 'format', '%(asctime)s [%(name)s][%(process)5d] %(levelname)s: %(message)s'),
            Config.get_value(log, 'maxBytes', 536870912),
            Config.get_value(log, 'backupCount', 10),
        )

    def get_credential(self):
        log = self.cfg.get('credential', {}) if self.cfg is not None else None
        return CredentialConf(
            certDir=Config.get_value(log, 'certDir', ''),
            enable=Config.get_value(log, 'enable', True)
        )

    def get_server(self):
        server = self.cfg.get('server', {}) if self.cfg is not None else None
        return ServerConf(
            Config.get_value(server, 'port', 9401),  # 9003 → 9401
            Config.get_value(server, 'cacheDir', '.cache'),
        )

    def get_database(self):
        database = self.cfg.get('database', {}) if self.cfg is not None else None
        return DatabaseConfig(
            type=database.get('type'),
            host=database.get('host'),
            port=int(database.get('port')),
            user=database.get('user'),
            password=database.get('password'),
            name=database.get('name')
        )

    @staticmethod
    def get_value(obj, key, default):
        if obj is None:
            return default

        value = obj.get(key)
        return value if value is not None else default

    def configLog(self):
        log = self.get_log()
        dirname = os.path.dirname(log.filename)
        if len(dirname) > 0 and not os.path.exists(dirname):
            os.makedirs(dirname)

        for handler in logging.root.handlers[:]:
            logging.info('remove the handler={}'.format(handler))
            logging.root.removeHandler(handler)

        handlers = [RotatingFileHandler(filename=log.filename, maxBytes=log.maxBytes, backupCount=log.backupCount)]
        logging.basicConfig(handlers=handlers, level=log.level, format=log.format)
        logging.info('Log configs={}'.format(log))
