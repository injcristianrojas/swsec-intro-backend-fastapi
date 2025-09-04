from sqlmodel import Field, Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///db.sqlite"

engine = create_engine(DATABASE_URL, echo=True)


class MessageBase(SQLModel):
    message: str


class Message(MessageBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class MessageInsert(MessageBase):
    pass


class UserBase(SQLModel):
    username: str
    password: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_type: int


class UserLogin(UserBase):
    pass


class Token(SQLModel):
    token: str


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
