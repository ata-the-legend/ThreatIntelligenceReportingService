from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class SuspiciousIP(Base):
    
    __tablename__ = 'suspiciousIPs'

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String)
    report_count = Column(Integer, default=1)
    last_reported = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)