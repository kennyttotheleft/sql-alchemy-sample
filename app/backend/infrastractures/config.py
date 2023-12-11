# coding=utf-8

import os

class DatabaseConf:
    def __init__(self, user: str, password: str, name: str, host: str, port: str):
        self.user = user
        self.password = password
        self.name = name
        self.host = host
        self.port = port

def get_db_cfg() -> DatabaseConf:
  return DatabaseConf(
      user=os.getenv('DB_USER'),
      password=os.getenv('DB_PASS'),
      name=os.getenv('DB_NAME'),
      host=os.getenv('DB_HOST'),
      port=os.getenv('DB_PORT'))

