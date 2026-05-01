from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Style(Base):
    __tablename__ = "styles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))


class RequestHistory(Base):
    __tablename__ = "request_history"
    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)
    adapted_text = Column(Text, nullable=True)
    target_style = Column(String(50))
    created_at = Column(DateTime, server_default=func.now())
