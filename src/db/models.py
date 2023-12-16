from __future__ import annotations

import enum
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, UUID, Boolean, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.sql import expression, func

Base = declarative_base()


class DealType(enum.Enum):
    buy = "buy"
    sell = "sell"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String)
    deals: Mapped[list[Deal]] = relationship(
        back_populates="user",
        cascade="all, delete",
    )
    bots: Mapped[list[Bot]] = relationship(
            back_populates="user",
            cascade="all, delete",
            )


class Instrument(Base):
    __tablename__ = "instruments"

    code: Mapped[str] = mapped_column(String(30), primary_key=True)
    title: Mapped[str] = mapped_column(String)
    group: Mapped[str] = mapped_column(String(30))
    has_model: Mapped[bool] = mapped_column(Boolean, server_default=expression.false())
    deals: Mapped[list[Deal]] = relationship(
        back_populates="instrument",
        cascade="all, delete",
    )

    def __repr__(self) -> str:
        return f"Instrument(code={self.code}, title={self.title})"


class Deal(Base):
    __tablename__ = "deals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price: Mapped[Decimal]
    quantity: Mapped[int]
    deal_type: Mapped[DealType] = mapped_column(Enum(DealType))
    date_time: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="deals")
    instrument_code: Mapped[str] = mapped_column(ForeignKey("instruments.code"))
    instrument: Mapped[Instrument] = relationship(back_populates="deals")
    balance: Mapped[Decimal] = mapped_column(DECIMAL)

    def __repr__(self) -> str:
        return f"Deal(id={self.id}, price={self.price}, quantity={self.quantity}, deal_type={self.deal_type}, user_id={self.user_id}, instrument_code={self.instrument_code}, balance={self.balance})"

class Bot(Base):
    __tablename__ = "bots"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("users.id"), primary_key=True)
    instrument_code: Mapped[str] = mapped_column(String(30), primary_key=True)
    status: Mapped[bool] = mapped_column(Boolean, server_default=expression.false())
    start_balance: Mapped[Decimal] = mapped_column(DECIMAL, nullable=True, default = 0.00)
    user: Mapped[User] = relationship(back_populates="bots")

