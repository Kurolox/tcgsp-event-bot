from sqlalchemy import Column, Integer, ForeignKey
from schemas.base import Base


class Battle(Base):
    __tablename__ = "tamers"

    id = Column(Integer, primary_key = True)
    currency = Column(Integer)
    current_battle = Column(Integer, ForeignKey("battles.id"))