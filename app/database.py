from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

SQLALCHEMY_DATABASE_URL = 'sqlite:///db.sqlite'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True, nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10), index=True, nullable=False)
    password = Column(String(10), index=True, nullable=False)
    user_type = Column(Integer, index=True, nullable=False)

def init_db():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    initial_data = [
        Message(message="Bienvenidos al foro de Fans de las Aves Chilenas. Soy el Administrador."),
        Message(message="Se informa que la API se encuentra deshabilitada hasta nuevo aviso."),
        User(username="zorzal", password="fio", user_type=2),
        User(username="admin", password="stgeddesudf", user_type=1),
        User(username="chincol", password="fiofio", user_type=2),
    ]
    session.add_all(initial_data)
    session.commit()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
