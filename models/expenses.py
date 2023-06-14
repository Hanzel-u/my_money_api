from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship
from config.database import Base

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    amount = Column(Numeric(precision=10, scale=2))
    id_type = Column(Integer, ForeignKey('types.id'))
    id_user = Column(Integer, ForeignKey('users.id'))

    type = relationship("Type", back_populates="expenses")
    user = relationship("User", back_populates="expenses")