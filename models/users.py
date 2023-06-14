from sqlalchemy import Column, Integer, String, Numeric
from config.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    budget = Column(Numeric(precision=10, scale=2))

    expenses = relationship("Expense", back_populates="user")