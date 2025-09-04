from sqlmodel import Field, Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///db.sqlite"

engine = create_engine(DATABASE_URL, echo=True)


class MessageBase(SQLModel):
    message: str


class Message(MessageBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class MessageInsert(MessageBase):
    pass


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    user_type: int


def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(
            Message(
                message="Bienvenidos al foro de Fans de las Aves Chilenas. Soy el Administrador."
            )
        )
        session.add(
            Message(
                message="Se informa que la API se encuentra deshabilitada hasta nuevo aviso."
            )
        )
        session.add(User(username="zorzal", password="fio", user_type=2))
        session.add(User(username="admin", password="stgeddesudf", user_type=1))
        session.add(User(username="chincol", password="fiofio", user_type=2))
        session.commit()
