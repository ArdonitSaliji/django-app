from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

mysqlEngine: Engine = create_engine(
    'mysql+pymysql://root:password@localhost',
    echo=True,  # use True in debug mode
    pool_pre_ping=True,
)
MySQLTableBase = declarative_base(mysqlEngine)


def MySqlSession(expireOnCommit: bool = False) -> Session:
    return sessionmaker(bind=mysqlEngine, expire_on_commit=expireOnCommit)()


def createMySQLTables():
    MySQLTableBase.metadata.create_all()


def dropMySQLTables():
    MySQLTableBase.metadata.drop_all()


# Example User orm
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import INTEGER, BIGINT, TINYINT, VARCHAR
from sqlalchemy import ForeignKey, Column, String, Boolean, Float, DateTime


class Products(MySQLTableBase):
    __tablename__ = 'products'

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    lastActive = Column(DateTime, onupdate=func.now())
    joinDate = Column(DateTime, server_default=func.now())