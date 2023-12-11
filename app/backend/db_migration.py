# coding=utf-8

from backend.infrastractures.postgres import create_db_and_tables

# table registration
from models.user_model import UserModel

if __name__ == "__main__":
    create_db_and_tables()
