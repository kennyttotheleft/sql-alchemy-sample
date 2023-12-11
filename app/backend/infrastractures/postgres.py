# coding=utf-8

from contextlib import contextmanager
from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr
from sqlmodel import SQLModel, Session, Column, Field, DateTime, create_engine

from backend.infrastractures.config import DatabaseConf, get_db_cfg

def __get_db_dsl(cfg: DatabaseConf) -> str:
    return 'postgresql://{user}:{password}@{host}:{port}/{name}'\
          .format(
              user=cfg.user,
              password=cfg.password,
              host=cfg.host,
              port=cfg.port,
              name=cfg.name)

__engine = create_engine(
    __get_db_dsl(get_db_cfg()),
    echo=True)

BaseModel = SQLModel
RDBSession = Session

def create_db_and_tables():
    BaseModel.metadata.create_all(__engine)

@contextmanager
def get_db_context():
    db = Session(__engine)
    try:
        yield db
    finally:
        db.close()

class TimeStampMixin(object):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
        )

# TODO
# How to use Mixins? #70
# https://github.com/tiangolo/sqlmodel/issues/70
# class TimeStampMixin(BaseModel):
#     """Provides last created/modified timestamps"""
#
#     created_at: Optional[datetime] = Field(
#         sa_column=Column(
#             DateTime,
#             default=datetime.utcnow,
#             nullable=False,
#         )
#     )
#
#     updated_at: Optional[datetime] = Field(
#         sa_column=Column(
#             DateTime,
#             default=datetime.utcnow,
#             onupdate=datetime.utcnow,
#         )
#     )