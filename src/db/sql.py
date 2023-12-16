from logging import Logger
from time import sleep

from psycopg2 import OperationalError as psycopg2OpError
from sqlalchemy import URL, create_engine
from sqlalchemy.exc import OperationalError as sqlalchemyOpError
from sqlalchemy.orm import sessionmaker

from config.settings import settings
from src.db.models import Base
from src.utils.logger import conf_logger as logger


class SQLManager:
    instance = None

    def __init__(self, log: Logger = logger("__sql_manager__")):
        self.engine_url = URL.create(
            "postgresql+psycopg2",
            username=settings.postgres_user,
            password=settings.postgres_password,
            host=settings.postgres_host,
            port=settings.postgres_port_number,
            database=settings.postgres_db,
        )
        self.log = log
        connected = False
        while not connected:
            try:
                self._connect()
                self.log.debug("Database connected")
            except (sqlalchemyOpError, psycopg2OpError):
                self.log.warning("Database connection failed, retrying...")
                sleep(2)
            else:
                connected = True
        self._update_db()

    def __new__(cls, *args, **kwargs):
        """Singleton pattern"""
        if cls.instance is None:
            cls.instance = super(SQLManager, cls).__new__(cls)
        return cls.instance

    def __del__(self):
        """Close the database connection when the object is destroyed"""
        self._close()

    def _connect(self) -> None:
        """Connect to the postgresql database"""
        self.engine = create_engine(
            self.engine_url,
            pool_pre_ping=True,
        )
        Base.metadata.bind = self.engine
        db_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = db_session()

    def _close(self) -> None:
        """Closes the database connection"""
        self.session.close_all()

    def _update_db(self) -> None:
        """Create the database structure if it doesn't exist (update)"""
        # Create the tables if they don't exist
        Base.metadata.create_all(self.engine)

