from sqlalchemy import Column, Integer, Sequence, ForeignKey
from schemas.base import Base


class Battle(Base):
    __tablename__ = "battles"

    id = Column(Integer, Sequence("battle_id_sequence"), primary_key = True)
    tamer_1 = Column(Integer, ForeignKey("tamers.id"), nullable=False)
    tamer_2 = Column(Integer, ForeignKey("tamers.id"), nullable=False)