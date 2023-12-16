import uuid

from sqlalchemy import select

from src.auth.domain import Signup
from src.db.models import User
from src.db.repository import AbstractRepository
from src.db.schemas import Deal as DealSchema
from src.db.sql import SQLManager
from src.utils.logger import conf_logger as logger


class UserRepository(AbstractRepository):
    instance = None

    def __init__(self, db_manager: SQLManager) -> None:
        super().__init__()
        self.db = db_manager
        self.logger = logger("UserRepository")

    def __new__(cls, *args, **kwargs):
        """Singleton pattern"""
        if cls.instance is None:
            cls.instance = super(UserRepository, cls).__new__(cls)
        return cls.instance

    def add(
        self,
        user_data: Signup,
    ) -> User:
        user = User(**user_data.model_dump())
        self.db.session.add(user)
        self.db.session.commit()

        return user

    def get(
        self, user_id: uuid.UUID | None = None, email: str | None = None
    ) -> User | None:
        self.logger.debug("getting user by id %s or email %s", user_id, email)
        if user_id:
            return self.db.session.query(User).filter(User.id == user_id).first()
        elif email:
            return self.db.session.query(User).filter(User.email == email).first()
        else:
            raise ValueError("user_id or email must be provided")

    def update(self, user: User):
        self.db.session.add(user)
        self.db.session.commit()

    def delete(self, user_id: uuid.UUID | None = None, email: str | None = None):
        if user_id:
            self.db.session.query(User).filter(User.id == user_id).delete()
        elif email:
            self.db.session.query(User).filter(User.email == email).delete()
        else:
            raise ValueError("user_id or email must be provided")
        self.db.session.commit()

    def get_all(self) -> list[User]:
        return self.db.session.query(User).all()

