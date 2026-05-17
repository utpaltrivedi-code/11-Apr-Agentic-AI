import os
from datetime import datetime, timezone
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    source_id = Column(String, nullable=False)
    source_type = Column(String, nullable=False) 
    category = Column(String, nullable=False)      
    priority = Column(String, nullable=False)      
    title = Column(String, nullable=False)
    description = Column(Text)
    technical_details = Column(Text)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

def init_db():
    os.makedirs("data", exist_ok=True)
    engine = create_engine("sqlite:///data/feedback_system.db", echo=False)
    Base.metadata.create_all(engine)
    return engine

def get_session():
    return sessionmaker(bind=init_db())()