from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    icon = Column(Integer)

    expenses = relationship("Expense", back_populates="type")