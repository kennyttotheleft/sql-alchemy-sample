# coding=utf-8

from backend.infrastractures.postgres import RDBSession, get_db_context

# table registration
from models.user_model import UserModel

def __add_users(db: RDBSession):

    user_1 = UserModel(nickname="alice")
    user_2 = UserModel(nickname="bob", email="bob@example.com")
    user_3 = UserModel(nickname="charlie")

    db.add(user_1)
    db.add(user_2)
    db.add(user_3)

if __name__ == "__main__":
    with get_db_context() as db:
        __add_users(db)
        db.commit()